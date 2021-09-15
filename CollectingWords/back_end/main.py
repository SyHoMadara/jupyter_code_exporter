import sys
from PyQt5 import QtWidgets
from collections import deque

from CollectingWords.front_end.donewindow import Ui_Form
from CollectingWords.front_end.mainwindow import Ui_TabWidget
from CollectingWords.libs.file_tools import AskFileGraphical
from CollectingWords.libs.work_with_works_tools import PERSIAN_ALPHABET, ENGLISH_ALPHABET, NUMBERS


class WorkingWindow(Ui_Form):

    def setupUi(self, Form):
        super().setupUi(Form)

        # self.pushButtonDone.clicked.connect()


class MainWindow(Ui_TabWidget):

    def choose_base_file(self):
        """
        choose file with os explorer as base file that want collect from it.
        :return:
        """
        file = AskFileGraphical(file_type="Text File (*.txt);;All File (*)", r_w="r")
        self.lineEditBaseFilePath.setText(str(file.file_dir) + "\\" + file.file_name + file.file_extension)
        self.lineEditResultFilePath.setText(
            str(file.file_dir) + "\\" + file.file_name + ".result" + file.file_extension)
        self.lineEditResultFilePath.setSelection(0, 0)
        self.lineEditBaseFilePath.setSelection(0, 0)

    def choose_result_file(self):
        """
        choose file with os explorer as result file
        :return:
        """
        file = AskFileGraphical(file_type="Text File (*.txt);;All File (*)", r_w="w")
        self.lineEditResultFilePath.setText(
            str(file.file_dir) + "\\" + file.file_name + file.file_extension)
        self.lineEditResultFilePath.setSelection(0, 0)

    def combo_box_splitter_action(self, value):
        if value == "Custom":
            self.lineEditCustomSplitter.setEnabled(True)
            self.lineEditCustomSplitter.setText("")
        else:
            self.lineEditCustomSplitter.setEnabled(False)
            self.lineEditCustomSplitter.setText(self.comboBoxSplitter.currentText())

    def combo_box_detection_splitter_action(self, value):
        if value == "Custom":
            self.lineEditCustomDetection.setEnabled(True)
            self.lineEditCustomDetection.setText("")
        else:
            self.lineEditCustomDetection.setEnabled(False)
            self.lineEditCustomDetection.setText(self.comboBoxDetection.currentText())

    def get_accept_chars(self):
        chars = set()
        if self.checkBoxPersian.checkState():
            for letter in PERSIAN_ALPHABET:
                chars.add(letter)
        if self.checkBoxEnglish.checkState():
            for letter in ENGLISH_ALPHABET:
                chars.add(letter)
        if self.checkBoxNumber.checkState():
            for letter in ENGLISH_ALPHABET:
                chars.add(letter)
        for letter in self.lineEditIncludedChars.text():
            chars.add(letter)
        if self.checkBoxAll.checkState():
            chars = None
        return chars

    def check_start_requirement(self):
        ans = True
        # boothe path can't be empty
        if self.lineEditBaseFilePath.text() == "" or self.lineEditResultFilePath.text() == "":
            ans = False
            self.labelWarnings.setText("Path of base file or result file, hasn't chosen.")

        # splitter and directer must choose
        if self.comboBoxSplitter.currentText() == "Custom" and self.lineEditCustomSplitter.text() == "":
            self.labelWarnings.setText("Separator most choose")
            ans = False
        if self.comboBoxDetection.currentText() == "Custom" and self.lineEditCustomDetection.text() == "":
            self.labelWarnings.setText("Detection splitter most choose")
            ans = False

        # check at least one character be include
        if not any([bool(self.checkBoxAll.checkState()), bool(self.checkBoxNumber.checkState()),
                    bool(self.checkBoxEnglish.checkState()),
                    bool(self.checkBoxPersian.checkState()), self.lineEditIncludedChars.text() != ""]):
            self.labelWarnings.setText("Include chars need at least one char")
            ans = False

        return ans

    def splitter_getter(self, splitter: str) -> str:
        if splitter == "Enter":
            return "\n"
        elif splitter == "Space":
            return " "
        elif splitter == "Coma":
            return ","
        return " "

    def create_working_window(self):
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        ui.pushButtonDone.clicked.connect(Form.close)
        self.workingWindowUi = ui
        self.workingWindow = Form

    def working_window_progress_bar_change_value(self, value):
        self.workingWindowUi.progressBar.setValue(value)

    def start(self):
        # check requirements:
        self.labelWarnings.setText("")
        if not self.check_start_requirement():
            return
        ENCODE = self.comboBoxEncode.currentText()
        result = ""
        file_string = ""
        replacements = []
        replacement_text = self.lineEditReplacements.text()
        if len(replacements) != 0:
            for i in range(0, int(len(replacement_text) / 2) + 1, 2):
                replacements.append((replacement_text[i], replacement_text[i + 1]))

        detection_splitter = self.splitter_getter(self.lineEditCustomDetection.text())
        splitter = self.splitter_getter(self.lineEditCustomSplitter.text())
        acceptCharacters = self.get_accept_chars()
        try:
            self.create_working_window()
            self.workingWindow.show()
            with open(self.lineEditBaseFilePath.text(), mode="r", encoding=ENCODE) as file:
                for line in file:
                    file_string += line
                    file_string += "\n"
                file.close()
            # 10%
            self.working_window_progress_bar_change_value(25)

            for letter in file_string:
                if not bool(replacements):
                    for replacement in replacements:
                        letter.replace(replacement[0], replacement[1])
                if acceptCharacters is not None and letter in acceptCharacters:
                    result += letter
            words = result.split(detection_splitter)
            last_result = ""
            self.working_window_progress_bar_change_value(50)
            # sort
            if self.checkBoxSortWords.checkState():
                words.sort()

            # remove same words
            if self.checkBoxMakeUniqWords.checkState():
                word_set = set()
                for word in words:
                    word_set.add(word)
                words = word_set

            for word in words:
                if len(word) != 0:
                    last_result += word + splitter
            self.working_window_progress_bar_change_value(75)
            with open(self.lineEditResultFilePath.text(), mode="w", encoding=ENCODE) as file:
                file.write(last_result)
                file.close()
            self.working_window_progress_bar_change_value(100)


        except Exception as ex:
            self.labelWarnings.setText(str(ex))
            print(str(ex))

    def exit(self):
        sys.exit(app.exec_())

    def setupUi(self, TabWidget):
        super().setupUi(TabWidget)
        self.comboBoxSplitter.currentTextChanged.connect(self.combo_box_splitter_action)
        self.comboBoxDetection.currentTextChanged.connect(self.combo_box_detection_splitter_action)
        self.btnBrowsResult.clicked.connect(self.choose_result_file)
        self.btnBrowsResource.clicked.connect(self.choose_base_file)
        self.pushButtonStart.clicked.connect(self.start)
        self.pushButtonCancel.clicked.connect(self.exit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tabWidget = QtWidgets.QTabWidget()
    mainWindow = MainWindow()
    mainWindow.setupUi(tabWidget)
    tabWidget.show()
    sys.exit(app.exec_())
