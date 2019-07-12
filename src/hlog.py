DBG_LEVEL = 1
DGB_LEVEL_D = 1

class Log():
    def __init__(self):
        ''' '''

    @staticmethod
    def d(msg):
        if DBG_LEVEL >= DGB_LEVEL_D:
            print(msg)




