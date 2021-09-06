# encoding: utf-8
from pathlib import Path
import os
import PySide2.QtWidgets as qt
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox


class MainD(QWidget):
    def __init__(self):
        super(MainD, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "MainDialog/mainDialog.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        self.ui.btnShowAutoTradeDialog.clicked.connect(self.showAutoTradeDialog)
        ui_file.close()

    def showAutoTradeDialog(self):
        qt.QMessageBox(self, "asdf", "dasf")
