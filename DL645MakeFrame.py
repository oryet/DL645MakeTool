from PublicLib import public as pub
from PublicLib.Protocol.dl645format import *


def CalSum(l):
    s = sum(l)
    s = abs(s)
    s = int(s)
    return s

def loadCfg(dt):
    Config = {}
    dt['rtn'] = False
    try:
        if 'fileName' in dt:
            Config = pub.loadDefaultSettings(dt['fileName'])
            if 'FrameHead' in Config:
                dt['FrameHead'] = Config['FrameHead']
            if 'MtrAddr' in Config:
                dt['MtrAddr'] = Config['MtrAddr']
            if 'Ctrl' in Config:
                dt['Ctrl'] = Config['Ctrl']
            if 'DI' in Config:
                dt['DI'] = Config['DI']
            dt['rtn'] = True
    except:
        dt['msg'] = 'mtrCali.json does not exist!'
    return Config

def makeTempCaliData(dt):
    dt['fileName'] = "cfgTemp.json"
    Config = loadCfg(dt)
    if dt['rtn']:
        num = Config['dataNum']
        VolList = Config['VolList']
        AmpList = Config['AmpList']
        ZoneAmpList = Config['ZoneAmpList']
        dt['parm'] = [num, VolList, AmpList, ZoneAmpList]

        s1 = CalSum(VolList)
        s2 = CalSum(AmpList)
        s3 = CalSum(ZoneAmpList)

        s = ''
        # 数量
        # s += dl645_xxxxxxxx2hex(num, 1)
        # 电压补偿
        for i in range(num):
            s += dl645_xxxx2hex(VolList[i], 1)
        # 电流补偿
        for i in range(num):
            s += dl645_xxxx2hex(AmpList[i], 1)
        # 零线 电流补偿
        for i in range(num):
            s += dl645_xxxx2hex(ZoneAmpList[i], 1)

        # 校验
        s += dl645_xxxx2hex(s1, 1)
        s += dl645_xxxx2hex(s2, 1)
        s += dl645_xxxx2hex(s3, 1)
        # print('\n', 's1=', s1, 's2=', s2)

        dt['rtn'] = True
        dt['data'] = s
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgTemp.json does not exist!'

def makeMtrCaliData(dt):
    dt['fileName'] = "cfgMtrCali.json"
    cfg = loadCfg(dt)
    if dt['rtn']:
        s = ''
        # 密码 (4字节)
        for d in cfg['Password']:
            a = hex(ord(d)).replace('0x', '00')
            s += a[-2:]
        # (A/B/C)相电压(12字节)
        for d in cfg['Vol']:
            s += dl645_xxxx_xxxx2hex(d, t=HEX)
        # (A/B/C)相电流(12字节)
        for d in cfg['Amp']:
            s += dl645_xx_xxxxxx2hex(d, t=HEX)
        # (A/B/C)相有功功率(12字节)
        for d in cfg['PPwr']:
            s += dl645_xxxx_xxxx2hex(d, t=HEX)
        # (A/B/C)相无功功率(12字节)
        for d in cfg['QPwr']:
            s += dl645_xxxx_xxxx2hex(d, t=HEX)
        # 脉冲常数(4字节)
        s += dl645_xxxxxxxx2hex(cfg['conste'], t=HEX)
        # 启动功率(4字节)
        s += dl645_xxxx_xxxx2hex(cfg['startip'], t=HEX)
        # 额定电压(2字节)
        s += dl645_xxx_x2hex(cfg['ub'], t=HEX)
        # 额定电流(2字节)
        s += dl645_x_xxx2hex(cfg['ib'], t=HEX)
        # 最大电流(2字节)
        s += dl645_xx_xx2hex(cfg['imax'], t=HEX)
        # 频率(1字节)
        s += dl645_xx2hex(cfg['freq'], t=HEX)
        # 接线模式(1字节)
        s += dl645_xx2hex(cfg['wriemode'], t=HEX)
        # 接入模式(1字节)
        s += dl645_xx2hex(cfg['inmode'], t=HEX)
        # 能量累加模式(1字节)
        s += dl645_xx2hex(cfg['addmode'], t=HEX)
        # 有功等级(1字节)
        s += dl645_xx2hex(cfg['pclass'], t=HEX)
        # 无功等级(1字节)
        s += dl645_xx2hex(cfg['qclass'], t=HEX)
        # 电压增益(1字节)
        s += dl645_xx2hex(cfg['volgain'], t=HEX)
        # 电流增益(1字节)
        s += dl645_xx2hex(cfg['ampgain'], t=HEX)

        dt['data'] = s
        dt['rtn'] = True
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgMtrCali.json does not exist!'

def makeMtrCaliData_ZeroLine(dt):
    dt['fileName'] = "cfgMtrCali.json"
    cfg = loadCfg(dt)
    if dt['rtn']:
        s = ''
        dt['DI'] = 'F6FF'
        # 密码 (4字节)
        for d in cfg['Password']:
            a = hex(ord(d)).replace('0x', '00')
            s += a[-2:]
        # (A/B/C)相电流(12字节)
        for d in cfg['ZeroLineAmp']:
            s += dl645_xx_xxxxxx2hex(d, t=HEX)

        dt['data'] = s
        dt['rtn'] = True
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgMtrCali.json does not exist!'

def makeMtrCaliData_ZeroLineOffset(dt):
    dt['fileName'] = "cfgMtrCali.json"
    cfg = loadCfg(dt)
    if dt['rtn']:
        s = ''
        dt['DI'] = 'F7FF'
        # 密码 (4字节)
        for d in cfg['Password']:
            a = hex(ord(d)).replace('0x', '00')
            s += a[-2:]

        dt['data'] = s
        dt['rtn'] = True
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgMtrCali.json does not exist!'

def makeMtrCaliData_DataPowerOffset(dt):
    dt['fileName'] = "cfgMtrCali.json"
    cfg = loadCfg(dt)
    if dt['rtn']:
        s = ''
        dt['DI'] = 'F8FF'
        # 密码 (4字节)
        for d in cfg['Password']:
            a = hex(ord(d)).replace('0x', '00')
            s += a[-2:]
        # (A/B/C)相电流(12字节)
        for d in cfg['PowerOffset']:
            s += dl645_xx_xxxxxx2hex(d, 1, t=BCD)

        dt['data'] = s
        dt['rtn'] = True
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgMtrCali.json does not exist!'

def makeMtrVirtualData_Ins(dt):
    dt['fileName'] = "MtrVirtual.json"
    cfg = loadCfg(dt)
    if dt['rtn']:
        s = ''
        dt['DI'] = '700000F0'
        # Ua,Ub,Uc
        for d in cfg['Vol']:
            s += dl645_xxx_x2hex(d, t=BCD)
        # Ia,Ib,Ic,In
        for d in cfg['Amp']:
            s += dl645_xx_xxxxxx2hex(d, t=BCD)
        # PhUa,PhUb,PhUc,PhIa,PhIb,PhIc,AngleA,AngleB,AngleC,PhIc-PhIa
        for d in cfg['Arc']:
            s += dl645_xxx_x2hex(d, t=BCD)
        # 电压频率
        for d in cfg['Frequency']:
            s += dl645_xxx_x2hex(d, t=BCD)

        dt['data'] = s
        dt['rtn'] = True
    else:
        dt['rtn'] = False
        dt['msg'] = 'cfgMtrCali.json does not exist!'

if __name__ == '__main__':
    dt = {}
    dt['fileName'] = "cfgMtrCali.json"
    makeMtrCaliData(dt)
    print(dt)