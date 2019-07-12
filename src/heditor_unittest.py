import unittest
import os
import memodata
import configmanager

class TestMemodata(unittest.TestCase):
    def test_memodata(self):
        memo = memodata.MemoData(name="1", data="2")
        self.assertTrue(memo.OnGetName() == "1")
        self.assertTrue(memo.OnGetData() == "2")
        memo.OnClear()
        self.assertTrue(memo.OnGetData() == "")

    def test_configmanager(self):
        cm = configmanager.ConfigManager()
        configmanager.OnLoadConfig("heidtor.cfg")

if __name__ == '__main__':
    unittest.main()