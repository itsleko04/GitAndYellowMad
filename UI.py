from PyQt6 import QtCore, QtWidgets


class UI_MyWidget(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(QtCore.QRect(0, 0, 418, 411))
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 330, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MyWidget", "Form"))
        self.pushButton.setText(_translate("MyWidget", "Сгенерировать"))
