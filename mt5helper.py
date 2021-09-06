import MetaTrader5 as mt5
import PySide2.QtWidgets as qt


class mt5Helper(object):
    def __init__(self):
        print(123)

    @staticmethod
    def login(obj, account, password, server):
        # 显示有关MetaTrader 5程序包的数据
        print("MetaTrader5 package author: ", mt5.__author__)
        print("MetaTrader5 package version: ", mt5.__version__)

        # 建立MetaTrader 5到指定交易账户的连接
        if not mt5.initialize(login=int(account), server=server, password=password):
            print("Login fail"+mt5.last_error())
            return False
        else:
            print(mt5.last_error())
            res = mt5.login(login=int(account), server=server, password=password)
            return res
