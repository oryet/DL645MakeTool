from PublicLib import public as pub
from PublicLib.Protocol.dl645resp import *
from PublicLib.Protocol.dl645 import *
from PublicLib.Protocol.dl645format import *


def CalSum(l):
    s = sum(l)
    s = abs(s)
    s = int(s)
    return s

def loadCfg(dt):
    Config = {}
    try:
        if 'FrameHead' in dt:
            Config = pub.loadDefaultSettings(dt['fileName'])
            if 'FrameHead' in dt:
                dt['FrameHead'] = Config['FrameHead']
            if 'MtrAddr' in dt:
                dt['MtrAddr'] = Config['MtrAddr']
            if 'Ctrl' in dt:
                dt['Ctrl'] = Config['Ctrl']
            if 'DI' in dt:
                dt['DI'] = Config['DI']
            dt['rtn'] = True
    except:
        dt['rtn'] = False
        dt['msg'] = 'mtrCali.json does not exist!'
    return Config

def makeTempCaliData(dt):
    dt['fileName'] = "cfgTemp.json"
    Config = loadCfg(dt)
    if dt['rtn']:
        num = Config['dataNum']
        tempList = Config['tempList']
        vrefList = Config['vrefList']

        s1 = CalSum(tempList)
        s2 = CalSum(vrefList)

        s = ''
        # 数量
        s += dl645_xxxxxxxx2hex(num, 1)
        # 温度
        for i in range(num):
            s += dl645_xxxxxxx_x2hex(tempList[i], 1)
        # 补偿
        for i in range(num):
            s += dl645_xxxxxxx_x2hex(vrefList[i], 1)

        # 校验
        s += dl645_xxxxxxxx2hex(s1, 1)
        s += dl645_xxxxxxxx2hex(s2, 1)
        # print('\n', 's1=', s1, 's2=', s2)

        dt['rtn'] = True
        dt['data'] = s
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgTemp.json does not exist!'

def makeMtrCaliData(dt):
    dt['fileName'] = "cfgMtrCali.json"
    Config = loadCfg(dt)
    if dt['rtn']:

        # data = ''
        # dl645data = dl['dl645data']
        s = ''
        dt['data'] = s
        dt['rtn'] = True
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgMtrCali.json does not exist!'