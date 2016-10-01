mainwindow.py:	mainwindow.ui
	pyuic4 -x mainwindow.ui -o mainwindow.py

all:	mainwindow.py

