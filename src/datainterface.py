class DataInterface:
    def __init__(self, data="", name = ""):
        self.Init(data, name)

    def OnClear(self):
        self.data = ""

    def Init(self, data="", name = ""):
        self.data = data
        self.name = name
        self.searchKeywordPos = []
        self.searchKeywordCurrentPos = -1

    def OnUpdateData(self, data):
        self.data = data

    def OnSetData(self, data):
        self.data = data

    def OnGetData(self):
        return self.data

    def OnSetName(self, name):
        self.name = name

    def OnGetName(self):
        return self.name

