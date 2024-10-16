# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 600)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.0454545, y1:0.454545, x2:1, y2:0, stop:0 rgba(118, 38, 65, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 61))
        self.label.setStyleSheet("\n"
"font: 48pt \"Showcard Gothic\";\n"
"background-color: transparent;\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 21))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"Algerian\";\n"
"background-color: transparent;\n"
"border: none;\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 90, 271, 20))
        self.lineEdit.setStyleSheet("background-color: transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 90, 71, 17))
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"font: 8pt \"Algerian\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.pushButton.setObjectName("pushButton")
        self.gridWidget = QtWidgets.QWidget(Dialog)
        self.gridWidget.setGeometry(QtCore.QRect(30, 180, 771, 141))
        self.gridWidget.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px; /* Optional: Adds rounded corners */")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.QTableWidget = QtWidgets.QTableWidget(self.gridWidget)
        self.QTableWidget.setStyleSheet("border: 2px solid white;\n"
"background-color: transparent;")
        self.QTableWidget.setObjectName("QTableWidget")
        self.QTableWidget.setColumnCount(8)
        self.QTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.QTableWidget, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(40, 330, 111, 16))
        self.comboBox.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(11, "")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 330, 91, 16))
        self.pushButton_2.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 87 8pt \"Arial Black\";\n"
"color:white")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 390, 91, 16))
        self.lineEdit_2.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 390, 91, 16))
        self.comboBox_2.setStyleSheet("border: 1px solid white;\n"
"font: 87 8pt \"Arial Black\";\n"
"background-color: transparent;\n"
"color:white;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 420, 51, 16))
        self.pushButton_3.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 87 8pt \"Arial Black\";\n"
"color:white")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(530, 120, 321, 21))
        self.label_3.setStyleSheet("font: 12pt \"Showcard Gothic\";\n"
"background-color: transparent;\n"
"color:black;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 150, 71, 16))
        self.lineEdit_3.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(610, 150, 61, 16))
        self.comboBox_3.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 75 8pt \"Arial Black\";\n"
"color:white")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(680, 150, 61, 16))
        self.lineEdit_4.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 150, 231, 16))
        self.progressBar.setStyleSheet("border: 1px solid #1e1e1e; /* Optional: Customize the border */\n"
"    text-align: center;        /* Optional: Align text in the center */\n"
"    color: white;      \n"
"background-color: transparent; /*\n"
" ")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 120, 51, 17))
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"font: 8pt \"Algerian\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 120, 51, 17))
        self.pushButton_7.setStyleSheet("background-color: transparent;\n"
"font: 9pt \"Algerian\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.pushButton_7.setObjectName("pushButton_7")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1, 391))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 376))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(40, 360, 141, 16))
        self.progressBar_2.setStyleSheet("border: 1px solid #1e1e1e; /* Optional: Customize the border */\n"
"    text-align: center;        /* Optional: Align text in the center */\n"
"    color: white;      \n"
"background-color: transparent; /*\n"
" ")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 150, 51, 16))
        self.pushButton_5.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 87 9pt \"Arial Black\";\n"
"color:white")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(580, 330, 321, 21))
        self.label_4.setStyleSheet("\n"
"background-color: transparent;\n"
"color:black;\n"
"font: 12pt \"Showcard Gothic\";")
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(600, 360, 111, 20))
        self.comboBox_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(11, "")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(490, 360, 111, 20))
        self.comboBox_5.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(7, "")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(710, 360, 111, 20))
        self.comboBox_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setItemText(7, "")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 390, 91, 16))
        self.pushButton_6.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 87 8pt \"Arial Black\";\n"
"color:white")
        self.pushButton_6.setObjectName("pushButton_6")
        self.timeLabel = QtWidgets.QLabel(Dialog)
        self.timeLabel.setGeometry(QtCore.QRect(190, 360, 161, 16))
        self.timeLabel.setStyleSheet("\n"
"font: 6pt \"Arial Black\";\n"
"background-color: transparent;\n"
"border: none;\n"
"color:white")
        self.timeLabel.setText("")
        self.timeLabel.setObjectName("timeLabel")
        self.timeLabel_2 = QtWidgets.QLabel(Dialog)
        self.timeLabel_2.setGeometry(QtCore.QRect(720, 390, 181, 16))
        self.timeLabel_2.setStyleSheet("\n"
"font: 6pt \"Arial Black\";\n"
"background-color: transparent;\n"
"border: none;\n"
"color:white")
        self.timeLabel_2.setText("")
        self.timeLabel_2.setObjectName("timeLabel_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "             ScrapeSort Nexus"))
        self.label_2.setText(_translate("Dialog", "Enter"))
        self.pushButton.setText(_translate("Dialog", "Scrapp Data"))
        item = self.QTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Rows"))
        item = self.QTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Phone Names"))
        item = self.QTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Condition"))
        item = self.QTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Price"))
        item = self.QTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Shipping Cost"))
        item = self.QTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Location"))
        item = self.QTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Seller Info"))
        item = self.QTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Quantity Sold"))
        self.comboBox.setItemText(0, _translate("Dialog", "Bubble Sort"))
        self.comboBox.setItemText(1, _translate("Dialog", "Selection Sort"))
        self.comboBox.setItemText(2, _translate("Dialog", "Insertion Sort "))
        self.comboBox.setItemText(3, _translate("Dialog", "Merge Sort "))
        self.comboBox.setItemText(4, _translate("Dialog", "Quick Sort"))
        self.comboBox.setItemText(5, _translate("Dialog", "Counting Sort"))
        self.comboBox.setItemText(6, _translate("Dialog", "Radix Sort"))
        self.comboBox.setItemText(7, _translate("Dialog", "Bucket Sort"))
        self.comboBox.setItemText(8, _translate("Dialog", "Heapify Sort"))
        self.comboBox.setItemText(9, _translate("Dialog", "Cocktail Shaker Sort"))
        self.comboBox.setItemText(10, _translate("Dialog", "Shell Sort"))
        self.pushButton_2.setText(_translate("Dialog", "Sort Column"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Contains"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Starts withs"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Ends withs"))
        self.pushButton_3.setText(_translate("Dialog", "Search"))
        self.label_3.setText(_translate("Dialog", " Multi column Searching"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "AND"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "OR"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "NOT"))
        self.pushButton_4.setText(_translate("Dialog", "Pause"))
        self.pushButton_7.setText(_translate("Dialog", "Start"))
        self.pushButton_5.setText(_translate("Dialog", "Search"))
        self.label_4.setText(_translate("Dialog", " Multi column Sorting"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Bubble Sort"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Selection Sort"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Insertion Sort"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Merge Sort"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "Quick Sort"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "Counting Sort"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "Radix Sort"))
        self.comboBox_4.setItemText(7, _translate("Dialog", "Bucket Sort"))
        self.comboBox_4.setItemText(8, _translate("Dialog", "Heapify Sort"))
        self.comboBox_4.setItemText(9, _translate("Dialog", "Cocktail Shaker Sort"))
        self.comboBox_4.setItemText(10, _translate("Dialog", "Shell Sort"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Phone Name"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Condition"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Price"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Shipping Cost"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "Location"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "Seller Info"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "Quantity Sold"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "Phone Name"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "Condition"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "Price"))
        self.comboBox_6.setItemText(3, _translate("Dialog", "Shipping Cost"))
        self.comboBox_6.setItemText(4, _translate("Dialog", "Location"))
        self.comboBox_6.setItemText(5, _translate("Dialog", "Seller Info"))
        self.comboBox_6.setItemText(6, _translate("Dialog", "Quantity Sold"))
        self.pushButton_6.setText(_translate("Dialog", "Sort Column"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
