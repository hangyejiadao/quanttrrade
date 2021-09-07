# -*- coding: utf-8 -*- 
import os.path as osp
import sys
from MainDialog.Demo import  Demo
import unittest
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_TestLogin(self):
        # print("MetaTrader5 package author: ", mt5.__author__)
        # print("MetaTrader5 package version: ", mt5.__version__)
        # print(mt5.__version__)
        # # 建立MetaTrader 5到指定交易账户的连接
        # if  mt5.initialize(path="D:\\mt5\\terminal64.exe"):
        #     print(mt5.last_error())
        # res = mt5.login(login="500101676", server="ForexClub-MT5 Demo Serve", password="hxIpqAth")
        # if not res:
        #     print(mt5.last_error()) 
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ", mt5.__author__)
        print("MetaTrader5 package version: ", mt5.__version__)
        # establish MetaTrader 5 connection to a specified trading account
        if not mt5.initialize(login=500101676, server="ForexClub-MT5 Demo Serve", password="hxIpqAth"):
            print("initialize() failed, error code =", mt5.last_error())
        else:
            print("登录成功")
            # display data on connection status, server name and trading account
        # shut down connection to the MetaTrader 5 terminal

    def test_Test(self):
        de = Demo()
        print(123)
        print(123)

    def test_tick(self):
        print("MetaTrader5 package author: ", mt5.__author__)
        print("MetaTrader5 package version: ", mt5.__version__)

        # 导入'pandas'模块，用于以表格形式显示获得的数据
        import pandas as pd
        pd.set_option('display.max_columns', 500)  # number of columns to be displayed
        pd.set_option('display.width', 1500)  # max table width to display
        # 导入用于处理时区的pytz模块
        import pytz

        # 建立与MetaTrader 5程序端的连接
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            quit()

        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(2022,9, 7, tzinfo=timezone)
        # request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
        ticks = mt5.copy_ticks_from("XAUUSD", utc_from, 100000, mt5.COPY_TICKS_ALL)
        print("Ticks received:", len(ticks))

        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()

        # display data on each tick on a new line
        print("Display obtained ticks 'as is'")
        count = 0
        for tick in ticks:
            count += 1
            print(tick)
            if count >= 10:
                break

        # create DataFrame out of the obtained data
        ticks_frame = pd.DataFrame(ticks)
        # 将时间（以秒为单位）转换为日期时间格式
        ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

        # display data
        print("\nDisplay dataframe with ticks")
        print(ticks_frame.head(10))

    def test_tick(self):
        print("MetaTrader5 package author: ", mt5.__author__)
        print("MetaTrader5 package version: ", mt5.__version__)

        # 导入'pandas'模块，用于以表格形式显示获得的数据
        import pandas as pd
        pd.set_option('display.max_columns', 500)  # number of columns to be displayed
        pd.set_option('display.width', 1500)  # max table width to display
        # 导入用于处理时区的pytz模块
        import pytz

        # 建立与MetaTrader 5程序端的连接
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            quit()

        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(2022,9, 7, tzinfo=timezone)
        # request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
        ticks = mt5.copy_ticks_from("XAUUSD", utc_from, 100000, mt5.COPY_TICKS_ALL)
        print("Ticks received:", len(ticks))

        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()

        # display data on each tick on a new line
        print("Display obtained ticks 'as is'")
        count = 0
        for tick in ticks:
            count += 1
            print(tick)
            if count >= 10:
                break

        # create DataFrame out of the obtained data
        ticks_frame = pd.DataFrame(ticks)
        # 将时间（以秒为单位）转换为日期时间格式
        ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

        # display data
        print("\nDisplay dataframe with ticks")
        print(ticks_frame.head(10))     
     
if __name__ == '__main__':
    unittest.main()
