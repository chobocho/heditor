import os
import configparser
from hlog import *

class ConfigManager:
    def __init__(self):
       ''' '''

    @staticmethod
    def OnLoadConfig(filename = ""):
        Log.d("OnLoadConfig")
        if len(filename) == 0:
            return
        
        config = configparser.ConfigParser()
        config.read(filename)
        return config
        #if not hasattr(self, section):
        #Log.d(config['screen']['mode'])
    