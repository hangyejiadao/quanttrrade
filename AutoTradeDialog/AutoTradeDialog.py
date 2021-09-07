from pathlib import Path
import os
import PySide2.QtWidgets as qt
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
class MainD(QWidget):
    def __init__(self) -> None:
        super().__init__()
