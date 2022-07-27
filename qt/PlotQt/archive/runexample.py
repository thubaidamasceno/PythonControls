from PyQt5 import QtGui, QtWidgets, QtCore
import sys
from example import Window
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

if __name__ == "__main__":

    #start up GUI
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    main.raise_()

    #quit program on exit
    sys.exit(app.exec_())