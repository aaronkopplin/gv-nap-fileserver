from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from peer import Peer
import sys
import os


class PeerApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super(PeerApplication, self).__init__()
        os.system("pyuic5 -x GUI/gui.ui -o GUI/gui.py")  # compile the gui
        from GUI.gui import Ui_MainWindow  # import the newly compiled gui
        self.ui = Ui_MainWindow()  # create an instance of the GUI
        self.ui.setupUi(self)
        self.configure()
        self.peer = Peer()
        self.show()

    # override the closeEvent method
    def closeEvent(self, event):
        print ("User has clicked the red x on the main window")
        event.accept()

    def configure(self):
        self.ui.connect.clicked.connect(self.makeConnection)
        self.ui.search.clicked.connect(self.search)
        self.ui.go.clicked.connect(self.enterCommand)
        self.ui.results.setRowCount(2)
        self.ui.results.setColumnCount(2)
        self.ui.results.setItem(0, 0, QTableWidgetItem("First Name"))
        self.ui.results.setItem(0, 1, QTableWidgetItem("Last Name"))
        self.ui.results.setItem(1, 0, QTableWidgetItem("Aaron"))
        self.ui.results.setItem(1, 1, QTableWidgetItem("Kopplin"))

    def makeConnection(self):
        print("connecting to server: " + self.ui.server.text())
        self.peer.connect(self.ui.server.text(), int(self.ui.port.text()), self.ui.username.text(),
                          self.ui.hostname.text(), self.ui.speed.text())

    def search(self):
        print("searching server for \"" + self.ui.keyword.text() + "\"")

    def enterCommand(self):
        self.ui.commandLine.appendPlainText(">> " + self.ui.command.text())
        self.ui.command.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    peer_gui = PeerApplication()
    sys.exit(app.exec_())
