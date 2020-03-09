# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPK.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPK(object):
    def setupUi(self, AddPK):
        AddPK.setObjectName("AddPK")
        AddPK.resize(368, 174)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddPK)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(AddPK)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(AddPK)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddPK)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddPK)
        self.buttonBox.accepted.connect(AddPK.accept)
        self.buttonBox.rejected.connect(AddPK.reject)
        QtCore.QMetaObject.connectSlotsByName(AddPK)

    def retranslateUi(self, AddPK):
        _translate = QtCore.QCoreApplication.translate
        AddPK.setWindowTitle(_translate("AddPK", "Добавить показатель качества"))
        self.label.setText(_translate("AddPK", "Название показателя качества"))
