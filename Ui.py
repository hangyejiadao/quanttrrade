# This Python file uses the following encoding: utf-8

from pathlib import Path
import os
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

import mt5helper
from MainDialog.MainD import MainD


class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        self.ui.btnLogin.clicked.connect(self.login)
        ui_file.close()

    def login(self):
        account = self.ui.editAccount.text()
        password = self.ui.editPasswd.text()
        server = self.ui.editServer.text()
        loginres = mt5helper.mt5Helper.login(self, account, password, server)
        if loginres:
            QMessageBox.information(self, "成功登录", "成功登录")
            m_mainDialog = MainD()
            m_mainDialog.show()
