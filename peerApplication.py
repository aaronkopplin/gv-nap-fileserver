from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
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
        self.ui.server.setText("127.0.0.2")
        self.ui.port.setText("3000")
        self.ui.username.setText("username")
        self.ui.hostname.setText("hostname")
        self.ui.speed.addItem("Ethernet")
        self.ui.speed.addItem("Modem")
        self.ui.speed.addItem("T1")
        self.ui.speed.addItem("T3")

    def makeConnection(self, command=None, keyword=None):
        print("connecting to server: " + self.ui.server.text())
        if not command:
            command = 'connect'
        self.peer.connect(command, self.ui.server.text(), int(self.ui.port.text()), self.ui.username.text(),
                          self.ui.hostname.text(), self.ui.speed.currentText(), keyword=keyword)

    def search(self):
        print("searching server for \"" + self.ui.keyword.text() + "\"")
        self.makeConnection('search', keyword=self.ui.keyword.text())

        # Clear the current rows
        self.ui.results.setRowCount(0)

        # Display all of the files
        for file in self.peer.files:
            self.ui.results.insertRow(self.ui.results.rowCount())
            rowIndex = self.ui.results.rowCount() - 1
            self.ui.results.setItem(rowIndex, 0, QTableWidgetItem(file.find('speed').text))
            self.ui.results.setItem(rowIndex, 1, QTableWidgetItem(file.find('hostname').text))
            self.ui.results.setItem(rowIndex, 2, QTableWidgetItem(file.find('filename').text))

    def enterCommand(self):
        self.ui.commandLine.appendPlainText(">> " + self.ui.command.text())
        self.ui.command.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    peer_gui = PeerApplication()
    sys.exit(app.exec_())
