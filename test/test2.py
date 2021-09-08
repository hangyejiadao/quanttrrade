import unittest

from MetaTrader5 import *
import  MetaTrader5 as mt5
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

# 初始化 MT5 连接

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    # 实时读取mt5数据
    def test_A(self):
        mt5.initialize()

        sym = ['XAUUSDm']
        while True:
            # 将数据复制到数据帧
            d = pd.DataFrame()
            for i in sym:
                rates =mt5.copy_rates_from_pos(i, mt5.TIMEFRAME_M1, 0, 1)
                print(rates)
    def test_B(self):
        mt5.initialize()
        sym=["XAUUSDm"]
        while True:
            # 将数据复制到数据
            for i in sym:
                rate=mt5.
if __name__ == '__main__':
    unittest.main()
