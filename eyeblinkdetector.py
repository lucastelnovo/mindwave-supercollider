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

class EyeblinkDetector(object):
  def __init__(self, eyeblink_detected_callback=None, eyeblink_not_detected_callback=None):
    self.eyeblink_detected_callback = eyeblink_detected_callback
    self.eyeblink_not_detected_callback = eyeblink_not_detected_callback
    self.eyeblink_in_progress = False

  def check_eyeblink(self, sensitivity, low_freq, high_freq, raw_waves):
    import pyeeg
    spectrum, rel_spectrum = pyeeg.bin_power(raw_waves, [0.5, low_freq, high_freq,100], 512)
    if rel_spectrum[1] > float(sensitivity) and not self.eyeblink_in_progress:
      self.eyeblink_in_progress = True
      if self.eyeblink_detected_callback:
        self.eyeblink_detected_callback()
        return True

    elif rel_spectrum[1] <= float(sensitivity):
      self.eyeblink_in_progress = False
      if self.eyeblink_not_detected_callback:
        self.eyeblink_not_detected_callback()
        return False

    return False

