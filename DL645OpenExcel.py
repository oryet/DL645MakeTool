import xlrd

def openexel(path, SHEET_NUM):
    wb = xlrd.open_workbook(path)

    # 获得工作表的方法1
    sh = wb.sheet_by_index(SHEET_NUM)

    DI3 = sh.col_values(0)
    DI2 = sh.col_values(1)
    DI1 = sh.col_values(2)
    DI0 = sh.col_values(3)
    DIFormat = sh.col_values(4)
    DILen = sh.col_values(5)
    DIUnit = sh.col_values(6)
    DIName = sh.col_values(9)

    DIlist = []
    if DI3[0] == '数据标识' and DI3[1] == 'DI3' and DIFormat[0] == '数据格式'\
            and DILen[0] == '数据长度（字节）' and DIUnit[0] == '单位' and DIName[0] == '数据项名称':
        for i in range(2, len(DI3)):
            if DI3[i] == '…':
                continue

            DIlist += [DI2List([DI3[i], DI2[i], DI1[i], DI0[i]])]

    l = []

    return l

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

if __name__ == '__main__':
    path = r'F:\Work\NLY1502\需求和协议\NLY1502 NLY1220数据项定义表 - 2021-7-15(1).xlsx'
    l = openexel(path, 1)