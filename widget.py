# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication

import MetaTrader5 as mt5
from Ui import Ui
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if __name__ == "__main__":
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    app = QApplication([])
    wu = Ui()
    wu.show()
    
    sys.exit(app.exec_())
