##################################################################################
#      This file is part of mindwave-python.                                     #
#                                                                                #
#      mindwave-python is free software: you can redistribute it and/or modify   #
#      it under the terms of the GNU General Public License as published by      #
#      the Free Software Foundation, either version 3 of the License, or         #
#      (at your option) any later version.                                       #
#                                                                                #
#      mindwave-python is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#      GNU General Public License for more details.                              #
#                                                                                #
#      You should have received a copy of the GNU General Public License         #
#      along with mindwave-python.  If not, see <http://www.gnu.org/licenses/>.  #
##################################################################################

from collections import deque

from PyQt4 import QtCore, QtGui

import eyeblinkdetector
import mindwave
from mainwindow import Ui_MainWindow
import OSC

RAW_VAL_WIN_SIZE = 512
EYEBLINK_WIN_SIZE = 128
NO_OF_POINTS = 100




class MyMainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        """
        set up ui
        connect signals/slots
        """
        super(MyMainWindow, self).__init__()
        self.setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.running = False

        # connect signals and slots
        self.startButton.clicked.connect(self.monitor)
        self.MainWindow.update_ui_signal.connect(self.update_ui)
        self.MainWindow.update_statusbar_signal.connect(self.update_statusbar)

        # provide storage to remember the last 512 raw eeg data points
        self.last_512_raw_waves = deque([0] * RAW_VAL_WIN_SIZE, RAW_VAL_WIN_SIZE)
        self.counter = 0

        # setup eyeblink checker
        self.eyeblink_counter = 0
        self.eyeblink_in_progress = False
        self.eyeblink_detector = eyeblinkdetector.EyeblinkDetector(self.handle_blink_event)

        # statusbar text elements
        self.connected = "not connected"
        self.signal_quality = "unknown signal quality"
        self.update_statusbar()

        # make sure the menu entries do something
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

        port = 57120
        self.sc = OSC.OSCClient()
        try:
            self.sc.connect(('localhost', port)) #send locally to laptop
        except Exception as e:
            print ("Error connecting to supercollider: {0}".format(e))

    def monitor(self):
        """
        start/stop button pressed
        """
        print("monitor")
        if self.running:
            self.connected = "Not connected"
            self.signal_quality = "unknown signal quality"
            if self.h:
                self.h.serial_close()
            self.running = False
        else:
            self.connected = "Connected"
            self.signal_quality = "unknown signal quality"
            self.running = True
            self.h = None
            import serial
            try:
                device = self.deviceComboBox.currentText()
                self.h = mindwave.Headset("{0}".format(device))
            except serial.serialutil.SerialException as e:
                print("{0}".format(e))
                QtGui.QMessageBox.information(self.MainWindow, 'Couldn\'t find the headset',
                                              'Headset not found. Did you pair and connect to serial device {0}?'.format(
                                                  device), QtGui.QMessageBox.Ok)

            if self.h:
                self.h.raw_wave_handlers.append(self.raw_wave_handler)
                self.h.meditation_handlers.append(self.handle_meditation_event)
                self.h.attention_handlers.append(self.handle_attention_event)
                self.h.poor_signal_handlers.append(self.handle_poor_signal)
                self.h.good_signal_handlers.append(self.handle_good_signal)
                self.h.eeg_power_handlers.append(self.handle_eeg_power)
            else:
                self.running = False

        self.update_statusbar()

    def sendOscMsg(self, name="/signalquality", value=None):
        msg = OSC.OSCMessage()
        msg.setAddress(name)
        if value:
            msg.append(value)
        try:
            self.sc.send(msg)
        except Exception, e:
            print ("Error while sending msg {0} to supercollider: {1}".format(msg, e))
        print "Sent OSC Msg: ", msg

    def handle_poor_signal(self, headset, value):
        """
        react to a poor signal event
        """
        self.signal_quality = "poor signal quality {0}%".format(value)
        self.MainWindow.update_statusbar_signal.emit()
        self.sendOscMsg("/poorsignal")
        self.sendOscMsg("/signalquality", value)

    def handle_good_signal(self, headset, value):
        """
        handle to a good signal event
        """
        self.signal_quality = "good signal quality"
        self.MainWindow.update_statusbar_signal.emit()
        self.sendOscMsg("/goodsignal")
        self.sendOscMsg("/signalquality", value)

    def raw_wave_handler(self, headset, value):
        """
        callback function that accumulates raw eeg data
        for each new raw data point, a custom qt signal (update_ui_signal) is emitted
        """
        self.last_512_raw_waves.pop()
        self.last_512_raw_waves.appendleft(value)
        self.MainWindow.update_ui_signal.emit()
        self.sendOscMsg("/raw", value)

    def check_eyeblink(self, sensitivity, lowfreq, highfreq):
        """
        function that checks if last 128 raw eeg points contain an eye blink event
        """
        last_128_waves = list(self.last_512_raw_waves)[:EYEBLINK_WIN_SIZE]
        try:
            return self.eyeblink_detector.check_eyeblink(sensitivity, lowfreq, highfreq, last_128_waves)
        except ValueError:
            QtGui.QMessageBox.information(self.MainWindow, 'Eye blink sensitivity',
                                          'Invalid eyeblink sensitivity specified. Try 0.45 as a start.',
                                          QtGui.QMessageBox.Ok)
        return False

    def handle_blink_event(self):
        """
        function to do something if an eye blink event is detected
        """
        self.sendOscMsg("/eyeblink")

    def handle_meditation_event(self, headset, value):
        """
        function to do something when a meditation event is detected
        """
        self.sendOscMsg("/meditation", value)

    def handle_attention_event(self, headset, value):
        """
        function to do something when an attention event is detected
        """
        self.sendOscMsg("/attention", value)

    def handle_eeg_power(self, headset, delta, theta, lowalpha, highalpha, lowbeta, highbeta, lowgamma, midgamma):
        """
        function to do something when an eeg power event is detected
        """
        self.sendOscMsg("/eeg", [delta, theta, lowalpha, highalpha, lowbeta, highbeta, lowgamma, midgamma])

    def update_ui(self):
        """
        triggered whenever a raw eeg data point arrives
        """
        self.counter += 1

        if self.counter % EYEBLINK_WIN_SIZE == 0:
            self.counter = 0
            if self.check_eyeblink(self.eyeBlinkSensitivity.text(),
                                   self.lowerEyeBlinkFrequency.text(),
                                   self.higherEyeBlinkFrequency.text()):
                self.eyeblink_counter += 1

    def update_statusbar(self):
        self.statusbar.showMessage("{0} - {1}".format(self.connected, self.signal_quality))


class MainWindowWithCustomSignal(QtGui.QMainWindow):
    """
    specialized QtGui.MainWindow

    has to be specialized to let it react to a new qt signal
    (needed to update ui from callback function called from different thread)
    """
    update_ui_signal = QtCore.pyqtSignal()
    update_statusbar_signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindowWithCustomSignal, self).__init__(*args, **kwargs)


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Mindwave to OSC converter")
    win = MainWindowWithCustomSignal()
    ui = MyMainWindow(win)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
