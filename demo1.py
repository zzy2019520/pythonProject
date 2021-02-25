# -*- coding: utf-8 -*-
# @FileName: demo1.py
# @Author  : zzy
# @Time    : 2021/2/1 10:15
# @Software: PyCharm
file = open('D:/zzy/Desktop/text.txt', 'r')
file1 = open('D:/zzy/Desktop/a.txt', 'a+')
a = file.read()
print(a)
file1.write(a)
file.close()
file1.close()
