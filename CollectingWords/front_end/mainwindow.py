# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(750, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/pythonIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.setWindowIcon(icon)
        self.collecting = QtWidgets.QWidget()
        self.collecting.setObjectName("collecting")
        self.label_14 = QtWidgets.QLabel(self.collecting)
        self.label_14.setGeometry(QtCore.QRect(460, 130, 111, 20))
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(self.collecting)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 16))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.collecting)
        self.label_7.setGeometry(QtCore.QRect(330, 290, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.collecting)
        self.label_13.setGeometry(QtCore.QRect(400, 364, 311, 20))
        self.label_13.setObjectName("label_13")
        self.btnBrowsResource = QtWidgets.QPushButton(self.collecting)
        self.btnBrowsResource.setGeometry(QtCore.QRect(350, 30, 93, 31))
        self.btnBrowsResource.setObjectName("btnBrowsResource")
        self.label_3 = QtWidgets.QLabel(self.collecting)
        self.label_3.setGeometry(QtCore.QRect(330, 150, 141, 16))
        self.label_3.setObjectName("label_3")
        self.comboBoxSpliter = QtWidgets.QComboBox(self.collecting)
        self.comboBoxSpliter.setGeometry(QtCore.QRect(572, 100, 111, 22))
        self.comboBoxSpliter.setObjectName("comboBoxSpliter")
        self.comboBoxSpliter.addItem("")
        self.comboBoxSpliter.addItem("")
        self.comboBoxSpliter.addItem("")
        self.comboBoxSpliter.addItem("")
        self.lineEditCustomSpliter = QtWidgets.QLineEdit(self.collecting)
        self.lineEditCustomSpliter.setEnabled(False)
        self.lineEditCustomSpliter.setGeometry(QtCore.QRect(572, 130, 111, 22))
        self.lineEditCustomSpliter.setObjectName("lineEditCustomSpliter")
        self.label_11 = QtWidgets.QLabel(self.collecting)
        self.label_11.setGeometry(QtCore.QRect(470, 10, 81, 16))
        self.label_11.setObjectName("label_11")
        self.lineEditResultFilePath = QtWidgets.QLineEdit(self.collecting)
        self.lineEditResultFilePath.setGeometry(QtCore.QRect(30, 90, 311, 31))
        self.lineEditResultFilePath.setObjectName("lineEditResultFilePath")
        self.lineEditBaseFilePath = QtWidgets.QLineEdit(self.collecting)
        self.lineEditBaseFilePath.setGeometry(QtCore.QRect(32, 30, 311, 31))
        self.lineEditBaseFilePath.setObjectName("lineEditBaseFilePath")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.collecting)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(470, 30, 261, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxSortWords = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBoxSortWords.setObjectName("checkBoxSortWords")
        self.verticalLayout_3.addWidget(self.checkBoxSortWords)
        self.checkBoxMakeUniqWords = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBoxMakeUniqWords.setObjectName("checkBoxMakeUniqWords")
        self.verticalLayout_3.addWidget(self.checkBoxMakeUniqWords)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.collecting)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 220, 391, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxPersian = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxPersian.setObjectName("checkBoxPersian")
        self.horizontalLayout_2.addWidget(self.checkBoxPersian)
        self.checkBoxEnglish = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxEnglish.setObjectName("checkBoxEnglish")
        self.horizontalLayout_2.addWidget(self.checkBoxEnglish)
        self.checkBoxNumber = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxNumber.setObjectName("checkBoxNumber")
        self.horizontalLayout_2.addWidget(self.checkBoxNumber)
        self.checkBoxNonAlphabetChar = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxNonAlphabetChar.setObjectName("checkBoxNonAlphabetChar")
        self.horizontalLayout_2.addWidget(self.checkBoxNonAlphabetChar)
        self.btnBrowsResult = QtWidgets.QPushButton(self.collecting)
        self.btnBrowsResult.setGeometry(QtCore.QRect(350, 90, 93, 31))
        self.btnBrowsResult.setObjectName("btnBrowsResult")
        self.lineEditReplacements = QtWidgets.QLineEdit(self.collecting)
        self.lineEditReplacements.setGeometry(QtCore.QRect(330, 310, 331, 31))
        self.lineEditReplacements.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditReplacements.setClearButtonEnabled(True)
        self.lineEditReplacements.setObjectName("lineEditReplacements")
        self.label_8 = QtWidgets.QLabel(self.collecting)
        self.label_8.setGeometry(QtCore.QRect(400, 343, 311, 20))
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.collecting)
        self.label_5.setGeometry(QtCore.QRect(420, 200, 281, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.collecting)
        self.label_6.setGeometry(QtCore.QRect(540, 330, 121, 20))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.collecting)
        self.label_4.setGeometry(QtCore.QRect(540, 200, 121, 20))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEditIncludedChars = QtWidgets.QLineEdit(self.collecting)
        self.lineEditIncludedChars.setGeometry(QtCore.QRect(330, 170, 331, 31))
        self.lineEditIncludedChars.setToolTip("")
        self.lineEditIncludedChars.setStatusTip("")
        self.lineEditIncludedChars.setWhatsThis("")
        self.lineEditIncludedChars.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditIncludedChars.setClearButtonEnabled(True)
        self.lineEditIncludedChars.setObjectName("lineEditIncludedChars")
        self.pushButtonCancel = QtWidgets.QPushButton(self.collecting)
        self.pushButtonCancel.setGeometry(QtCore.QRect(500, 420, 101, 31))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.label_2 = QtWidgets.QLabel(self.collecting)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.label_2.setObjectName("label_2")
        self.widget_show_example = QtWidgets.QWidget(self.collecting)
        self.widget_show_example.setGeometry(QtCore.QRect(30, 170, 271, 261))
        self.widget_show_example.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 170, 0);\n"
"border-width: 3px;\n"
"border-style: inset;")
        self.widget_show_example.setObjectName("widget_show_example")
        self.label_12 = QtWidgets.QLabel(self.collecting)
        self.label_12.setGeometry(QtCore.QRect(470, 100, 101, 16))
        self.label_12.setObjectName("label_12")
        self.pushButtonStart = QtWidgets.QPushButton(self.collecting)
        self.pushButtonStart.setGeometry(QtCore.QRect(620, 420, 101, 31))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.label_9 = QtWidgets.QLabel(self.collecting)
        self.label_9.setGeometry(QtCore.QRect(50, 180, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.collecting)
        self.label_10.setGeometry(QtCore.QRect(50, 300, 91, 16))
        self.label_10.setObjectName("label_10")
        self.lbl_show_result_2 = QtWidgets.QLabel(self.collecting)
        self.lbl_show_result_2.setGeometry(QtCore.QRect(50, 330, 221, 81))
        self.lbl_show_result_2.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.lbl_show_result_2.setText("")
        self.lbl_show_result_2.setObjectName("lbl_show_result_2")
        self.lbl_show_result = QtWidgets.QLabel(self.collecting)
        self.lbl_show_result.setGeometry(QtCore.QRect(50, 210, 221, 81))
        self.lbl_show_result.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.lbl_show_result.setText("")
        self.lbl_show_result.setObjectName("lbl_show_result")
        TabWidget.addTab(self.collecting, "")
        self.adding = QtWidgets.QWidget()
        self.adding.setObjectName("adding")
        TabWidget.addTab(self.adding, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Word Collector"))
        self.label_14.setText(_translate("TabWidget", "Custom sepratetor"))
        self.label.setText(_translate("TabWidget", "Path to base file"))
        self.label_7.setText(_translate("TabWidget", "Replacement characters"))
        self.label_13.setText(_translate("TabWidget", "English char example: A,a means repalce A with a"))
        self.btnBrowsResource.setText(_translate("TabWidget", "Choose"))
        self.label_3.setText(_translate("TabWidget", "Include characters"))
        self.comboBoxSpliter.setItemText(0, _translate("TabWidget", "Enter"))
        self.comboBoxSpliter.setItemText(1, _translate("TabWidget", "Space"))
        self.comboBoxSpliter.setItemText(2, _translate("TabWidget", "Cama"))
        self.comboBoxSpliter.setItemText(3, _translate("TabWidget", "Custom"))
        self.label_11.setText(_translate("TabWidget", "Options"))
        self.checkBoxSortWords.setText(_translate("TabWidget", "Sort words"))
        self.checkBoxMakeUniqWords.setText(_translate("TabWidget", "Remove same words"))
        self.checkBoxPersian.setText(_translate("TabWidget", "Persian"))
        self.checkBoxEnglish.setText(_translate("TabWidget", "English"))
        self.checkBoxNumber.setText(_translate("TabWidget", "Number"))
        self.checkBoxNonAlphabetChar.setText(_translate("TabWidget", "Non alphabet character"))
        self.btnBrowsResult.setText(_translate("TabWidget", "Choose"))
        self.label_8.setText(_translate("TabWidget", "Persina char example: آ,ا means replace آ with ا"))
        self.label_5.setText(_translate("TabWidget", "Write them without any space or any gap"))
        self.pushButtonCancel.setText(_translate("TabWidget", "Cancel"))
        self.label_2.setText(_translate("TabWidget", "Path to result file"))
        self.label_12.setText(_translate("TabWidget", "Separate with"))
        self.pushButtonStart.setText(_translate("TabWidget", "Start"))
        self.label_9.setText(_translate("TabWidget", "Before changes"))
        self.label_10.setText(_translate("TabWidget", "After changes"))
        TabWidget.setTabText(TabWidget.indexOf(self.collecting), _translate("TabWidget", "Collecting"))
        TabWidget.setTabText(TabWidget.indexOf(self.adding), _translate("TabWidget", "Adding"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
