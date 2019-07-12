import wx
import os
from heditorframe import *

'''
Start  : 2019.07.12
'''
SW_TITLE = "HEditor V0.1105.SG15a"

def main(): 
    app = wx.App()
    frm = HEditorFrame(None, title=SW_TITLE, size=(800,800))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()