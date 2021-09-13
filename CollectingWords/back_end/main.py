import sys
from PyQt5 import QtWidgets

from CollectingWords.front_end.mainwindow import Ui_TabWidget
from CollectingWords.libs.file_tools import AskFileGraphical


class MainWindow(Ui_TabWidget):

    def choose_base_file(self):
        file = AskFileGraphical(file_type="Text File (*.txt);;All File (*)", r_w="r")
        self.baseFile = file
        self.lineEditBaseFilePath.setText(str(file.base_file))
        self.lineEditBaseFilePath.setSelection(0, 0)

    def choose_result_file(self):
        file = AskFileGraphical(file_type="Text File (*.txt);;All File (*)", r_w="w")
        self.resultFile = file
        self.lineEditResultFilePath.setText(str(file.base_file))
        self.lineEditResultFilePath.setSelection(0, 0)

    def setupUi(self, TabWidget):
        super().setupUi(TabWidget)
        self.btnBrowsResult.clicked.connect(self.choose_result_file)
        self.btnBrowsResource.clicked.connect(self.choose_base_file)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tabWidget = QtWidgets.QTabWidget()
    mainWindow = MainWindow()
    mainWindow.setupUi(tabWidget)
    tabWidget.show()
    sys.exit(app.exec_())
