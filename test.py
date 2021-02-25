# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 10:11
# @Author  : zzy
# @FileName: test.py
# @Software: PyCharm
from typing import TextIO
import cx_Oracle

# 将数据输出到文件，使用 file= fp
# a+ 如果文件不存在就创建，存在就在文件内容后边继续输出
fp: TextIO = open('D:/zzy/Desktop/text.txt', 'a+')

conn = cx_Oracle.connect('zzy/Zz123456@10.8.32.159:1521/oracle')  # 连接数据库
cursor = conn.cursor()  # 创建游标
phone = 17803858018
sql = "Select * from advice where phone = %s" % phone  # 查询语句
cursor.execute(sql)  # 执行sql语句
data = cursor.fetchall()  # 获取所有数据
for a in data:
    print(a, file=fp)
    # for b in a:
    #     print(b)

cursor.close()  # 关闭游标
conn.close()  # 关闭数据库连接
fp.close()

