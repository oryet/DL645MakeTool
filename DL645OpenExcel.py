import xlrd

def openSheet(sh):
    # wb = xlrd.open_workbook(path)

    # 获得工作表的方法1
    # sh = wb.sheet_by_index(SHEET_NUM)

    DI3 = sh.col_values(0)
    DI2 = sh.col_values(1)
    DI1 = sh.col_values(2)
    DI0 = sh.col_values(3)
    DIFormat = sh.col_values(4)
    DILen = sh.col_values(5)
    DIUnit = sh.col_values(6)
    DIName = sh.col_values(9)

    dl = {'DI':[], 'DIFormat':[], 'DILen':[], 'DIUnit':[], 'DIName':[]}

    if DI3[0] == '数据标识' and DI3[1] == 'DI3' and DIFormat[0] == '数据格式'\
            and DILen[0] == '数据长度（字节）' and DIUnit[0] == '单位' and DIName[0] == '数据项名称':
        for i in range(2, len(DI3)):
            if DI3[i] == '…' or DI3[i] == '':
                continue

            dl['DI'] += [DI2List([DI3[i], DI2[i], DI1[i], DI0[i]])]
            dl['DIFormat'] += [DIFormat[i]]
            dl['DILen'] += [DILen[i]]
            dl['DIUnit'] += [DIUnit[i]]
            dl['DIName'] += [DIName[i]]

    return dl

def DI2List(dl):
    dsl = ''
    for d in dl:
        if isinstance(d, float):
            ds = '00' + str(int(d))
            dsl += ds[-2:]
        elif isinstance(d, str):
            dsl += d[-2:]
        else:
            print('DI2List err')
    return dsl

def openExcel(path):
    pd = {'7.4.1电量':{}, '7.4.2参变量':{}, '7.4.3瞬时量':{}, '7.4.4曲线冻结':{}, '7.4.6日冻结':{}, '7.4.7月冻结':{}, \
          '7.4.7.1结算日':{}, '7.4.8电能表事件':{}, '7.4.9任务参数':{}, '7.4.10文件传输':{}, '7.4.11通信参数':{}, '7.4.14其他参数':{}}
    wb = xlrd.open_workbook(path)

    # 获得工作表的方法1
    for i,j in dict.items(pd):
        sh = wb.sheet_by_name(i)
        pd[i] = openSheet(sh)

    return  pd


if __name__ == '__main__':
    path = r'F:\Work\NLY1502\需求和协议\NLY1502 NLY1220数据项定义表 - 2021-7-15(1).xls'
    l = openExcel(path)
    print(l)