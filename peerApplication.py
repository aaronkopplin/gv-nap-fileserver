from PyQt5 import QtWidgets
import sys
import os

class PeerApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(PeerApplication, self).__init__()
        os.system("pyuic5 -x GUI/gui.ui -o GUI/gui.py")  # compile the gui
        from GUI.gui import Ui_MainWindow  # import the newly compiled gui
        ui = Ui_MainWindow()  # create an instance of the GUI
        ui.setupUi(self)
        self.show()

    # override the closeEvent method
    def closeEvent(self, event):
        print ("User has clicked the red x on the main window")
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    peer_gui = PeerApplication()
    sys.exit(app.exec_())
