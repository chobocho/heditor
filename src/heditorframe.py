import wx

class HEditorFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HEditorFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_CLOSE, self.onCloseApp)
 
        ctrl_Q_Id = wx.NewIdRef()
        self.Bind(wx.EVT_MENU, self.onClose, id=ctrl_Q_Id)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('Q'), ctrl_Q_Id )])
        self.SetAcceleratorTable(accel_tbl)

        self.splitter = wx.SplitterWindow(self, -1, wx.Point(0, 0), wx.Size(800, 800), wx.SP_3D | wx.SP_BORDER)
        # self.urlManger = UrlManager.UrlManager()
        #self.fileManagerPanel = ChoboFileManagerPanel.ChoboFileManagerPanel(self.splitter)
        #self.fileManagerPanel.setUrlManager(self.urlManger)
        #self.urlManagerPanel = ChoboUrlManagerPanel.ChoboUrlManagerPanel(self.splitter)
        #self.urlManagerPanel.setUrlManager(self.urlManger)
        #self.urlManagerPanel.drawUI()
        #self.splitter.SplitHorizontally(self.fileManagerPanel, self.urlManagerPanel)
        #self.splitter.SplitVertically(self.fileManagerPanel, self.urlManagerPanel)
        #self.splitter.SetMinimumPaneSize(20)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

        ico = wx.Icon('disk.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

    
    def onClose(self, event):
        self.Close()

    def onCloseApp(self, event):
        ''' '''
        #if event.CanVeto() and self.urlManagerPanel.needSave():
        #    try:
        #       self.urlManagerPanel.saveData()
        #    except:
        #       dlg = wx.MessageDialog(self, 'Exception happened during closing CFM!',
        #                'ChoboFileManager2', wx.OK | wx.ICON_INFORMATION)
        #       dlg.ShowModal()
        #       dlg.Destroy()
        self.Destroy()




