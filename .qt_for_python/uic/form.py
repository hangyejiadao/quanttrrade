# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(365, 543)
        self.btnLogin = QPushButton(Widget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(130, 230, 75, 23))
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 80, 168, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.editAccount = QLineEdit(self.layoutWidget)
        self.editAccount.setObjectName(u"editAccount")

        self.horizontalLayout.addWidget(self.editAccount)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 120, 31, 21))
        self.editPasswd = QLineEdit(Widget)
        self.editPasswd.setObjectName(u"editPasswd")
        self.editPasswd.setGeometry(QRect(110, 120, 131, 21))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 170, 51, 21))
        self.editServer = QLineEdit(Widget)
        self.editServer.setObjectName(u"editServer")
        self.editServer.setGeometry(QRect(110, 170, 131, 21))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btnLogin.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u8d26\u53f7:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u5bc6\u7801:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u670d\u52a1\u5668", None))
    # retranslateUi

