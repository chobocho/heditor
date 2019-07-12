import os
import configparser
from hlog import *

class ConfigManager:
    def __init__(self):
       ''' '''

def OnLoadConfig(filename = ""):
    Log.d("OnLoadConfig")
    if len(filename) == 0:
        return
    
    config = configparser.ConfigParser()
    config.read(filename)
    #if not hasattr(self, section):
    #Log.d(config['screen']['mode'])
    