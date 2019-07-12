from datainterface import *
from hlog import *

class MemoData(DataInterface):
    def __init__(self, data="", name = "default"):
        super(MemoData, self).__init__(data, name)

    def Init(self, data="", name = "default"):
        super().Init(data, name)




