# -*- coding: utf-8 -*-
# @FileName: PlansToBreakUp.py
# @Author  : zzy
# @Time    : 2021/2/23 16:42
# @Software: PyCharm
import sys
import xlrd
import xlwt
from datetime import datetime
from xlrd import xldate_as_tuple
import tkinter
import os
from tkinter import filedialog
from tkinter import messagebox

# Filepath = 'D:\zzy\Desktop\计划拆分程序开发需求\CX210202-1(2.6#-2.18#)整车8个产品250台-给编程-数控外协★模板★.xls'
saveColumn = ['任务号', '物料编码', '零件图号', '数量', '材质', '尺寸', '工序', '完工日期', '备料日期', '成型日期', '仓库', '定额', '工段', '组件', '外协', '批次']
tkinter.Tk().withdraw()  # 将Tkinter.Tk()实例隐藏
Filepath = filedialog.askopenfilename(title=u'选择文件')
Filename = os.path.basename(Filepath)
if Filepath == '':
    sys.exit()
'''读取工作表'''
data = xlrd.open_workbook(Filepath)
table = data.sheets()[0]
'''总行数'''
nrows = table.nrows
'''总列数'''
ncols = table.ncols

'''获取第二行的列名称'''
columnName = table.row_values(1)

'''获取需要的列的字典'''
columnNameDictionary = {}
for i in range(ncols):
    if columnName[i] in saveColumn:
        columnNameDictionary[columnName[i]] = i

'''获取需要的数据列数据，去掉不需要的列数据'''
dataContent = []
for key, value in columnNameDictionary.items():
    dataContent.append(table.col_values(value, start_rowx=1, end_rowx=nrows))

'''去掉不需要的行数据,同时将列表存储数据的方式由列转为行'''
ncols = len(dataContent)  # 列数量
nrows = len(dataContent[0])  # 行数量
finalDataContent = []

material = 0  # 材质的列号
for i in range(nrows):  # 找到材质的列号
    if dataContent[i][0] == '材质':
        material = i
        break

for i in range(nrows):
    temp = []
    if dataContent[material][i] != '——':
        for j in range(ncols):
            temp.append(dataContent[j][i])
        finalDataContent.append(temp)
        temp = []

'''更新列名字典'''
ncols = len(finalDataContent[0])  # 列数量
nrows = len(finalDataContent)  # 行数量
columnNameDictionary.clear()
for i in range(ncols):
    columnNameDictionary[finalDataContent[0][i]] = i

'''修改数据内容;按外协厂家进行分组-----为了减少循环次数放到了一块'''
outsourcSet = set()  # 创建外协集合
for i in range(nrows):
    if i > 0:  # 第一行为列名，从第二行开始遍历 “零件图号”列将所有字母改为小写、“.”改为“-”、“艺”改为“y”
        finalDataContent[i][columnNameDictionary['零件图号']] = finalDataContent[i][columnNameDictionary['零件图号']].lower()
        finalDataContent[i][columnNameDictionary['零件图号']] = finalDataContent[i][columnNameDictionary['零件图号']].replace(
            '.', '-')
        finalDataContent[i][columnNameDictionary['零件图号']] = finalDataContent[i][columnNameDictionary['零件图号']].replace(
            '艺', 'y')
        finalDataContent[i][columnNameDictionary['数量']] = int(finalDataContent[i][columnNameDictionary['数量']])
        finalDataContent[i][columnNameDictionary['完工日期']] = datetime(
            *xldate_as_tuple(finalDataContent[i][columnNameDictionary['完工日期']], 0)).strftime('%Y-%m-%d')
        finalDataContent[i][columnNameDictionary['备料日期']] = datetime(
            *xldate_as_tuple(finalDataContent[i][columnNameDictionary['备料日期']], 0)).strftime('%Y-%m-%d')
        finalDataContent[i][columnNameDictionary['成型日期']] = datetime(
            *xldate_as_tuple(finalDataContent[i][columnNameDictionary['成型日期']], 0)).strftime('%Y-%m-%d')
        outsourcSet.add(finalDataContent[i][columnNameDictionary['外协']])

outsourc = list(outsourcSet)

# 设置样式
# VERT_TOP = 0x00       上端对齐
# VERT_CENTER = 0x01    居中对齐（垂直方向上）
# VERT_BOTTOM = 0x02    低端对齐
# HORZ_LEFT = 0x01      左端对齐
# HORZ_CENTER = 0x02    居中对齐（水平方向上）
# HORZ_RIGHT = 0x03     右端对齐
style = xlwt.XFStyle()
al = xlwt.Alignment()
al.horz = 0x02  # 设置水平居中
al.vert = 0x01  # 设置垂直居中
style.alignment = al
for i in range(len(outsourc)):
    name = Filepath.replace('★模板★', '【' + outsourc[i] + '】')
    # 创建excel文件
    filename = xlwt.Workbook()
    # 给工作表命名
    sheet = filename.add_sheet(data.sheet_names()[0])
    a = b = 0
    for j in range(nrows):
        style2 = xlwt.easyxf('font:height 360;')  # 18pt,类型小初的字号
        row = sheet.row(j)
        row.set_style(style2)
        if j == 0:
            for k in range(ncols):
                sheet.write(a, b, finalDataContent[j][k], style)
                b += 1
            b = 0
            a += 1
        else:
            if finalDataContent[j][columnNameDictionary['外协']] == outsourc[i]:
                finalDataContent[j][columnNameDictionary['外协']] = '外协' + finalDataContent[j][columnNameDictionary['外协']]
                for k in range(ncols):
                    sheet.write(a, b, finalDataContent[j][k], style)
                    b += 1
                b = 0
                a += 1

    sheet.col(0).width = 256 * 14
    sheet.col(1).width = 256 * 14
    sheet.col(2).width = 256 * 20
    sheet.col(3).width = 256 * 5
    sheet.col(4).width = 256 * 10
    sheet.col(5).width = 256 * 20
    sheet.col(6).width = 256 * 20
    sheet.col(7).width = 256 * 14
    sheet.col(8).width = 256 * 14
    sheet.col(9).width = 256 * 14
    sheet.col(10).width = 256 * 10
    sheet.col(11).width = 256 * 10
    sheet.col(12).width = 256 * 14
    sheet.col(13).width = 256 * 14
    sheet.col(14).width = 256 * 14
    sheet.col(15).width = 256 * 20
    filename.save(name)

for i in range(len(outsourc)):
    name = Filepath.replace('★模板★.xls', '【' + outsourc[i] + '】.txt')
    txtData = open(name, 'w')
    count = 0  # 记录行号
    for j in range(nrows):
        if j > 0:
            if finalDataContent[j][columnNameDictionary['外协']] == '外协' + outsourc[i]:
                if count != 0:  # 如果不是第一行则先加换行再输出
                    print('', file=txtData)
                count += 1
                for k in range(ncols):
                    print(finalDataContent[j][k], end='\t', file=txtData)
    txtData.close()
messagebox.showinfo("提示", "文件分解完成")