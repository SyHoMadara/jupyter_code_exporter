import sys
from PyQt5 import QtWidgets

from CollectingWords.front_end.mainwindow import Ui_TabWidget
from CollectingWords.libs.file_tools import AskFileGraphical


class MainWindow(Ui_TabWidget):

    def choose_base_file(self):
        """
        choose file with os explorer as base file that want collect from it.
        :return:
        """
        file = AskFileGraphical(file_type="Text File (*.txt);;All File (*)", r_w="r")
        self.baseFile = file
        self.lineEditBaseFilePath.setText(str(file.base_file))
        self.lineEditBaseFilePath.setSelection(0, 0)

    def choose_result_file(self):
        """
        choose file with os explorer as result file
        :return:
        """
        file = AskFileGraphical(file_type="Text File (*.txt);;All File (*)", r_w="w")
        self.resultFile = file
        self.lineEditResultFilePath.setText(str(file.base_file))
        self.lineEditResultFilePath.setSelection(0, 0)

    def comboBoxSpliter_action(self, value):
        if value == "Custom":
            self.lineEditCustomSpliter.setEnabled(True)
        else:
            self.lineEditCustomSpliter.setEnabled(False)

    def start(self):
        ENCODE = self.lineEditEncode.text()
        result = ""
        file_string = ""
        acceptCharacter = ""
        for letter in self.lineEditIncludedChars.text():
            acceptCharacter += letter

        try:
            with open(self.lineEditBaseFilePath, mode="r", encoding=ENCODE) as file:
                for line in file:
                    file_string += file
                    file_string += "\n"
                file.close()
            for i in file_string:
                for letter in acceptCharecter:
                    pass

        except Exception as ex:
            self.labelWarnings.setText(str(ex))

    def setupUi(self, TabWidget):
        super().setupUi(TabWidget)
        self.comboBoxSpliter.currentTextChanged.connect(self.comboBoxSpliter_action)
        self.btnBrowsResult.clicked.connect(self.choose_result_file)
        self.btnBrowsResource.clicked.connect(self.choose_base_file)
        self.pushButtonStart.clicked.connect(self.start)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tabWidget = QtWidgets.QTabWidget()
    mainWindow = MainWindow()
    mainWindow.setupUi(tabWidget)
    tabWidget.show()
    sys.exit(app.exec_())
