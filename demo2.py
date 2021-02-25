# -*- coding: utf-8 -*-
# @FileName: demo2.py
# @Author  : zzy
# @Time    : 2021/2/1 10:30
# @Software: PyCharm
'''

用tk打开本地文件选择对话框

'''

import os

#print(os.listdir())

import tkinter

from tkinter import filedialog

#root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例

tkinter.Tk().withdraw()      # 将Tkinter.Tk()实例隐藏

# default_dir = r"C:\Users\Administrator"

#file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
# Filepath = filedialog.askopenfilename()
file_path = filedialog.askopenfilename(title=u'选择文件')
print(file_path)
print(os.path.basename(file_path))
# image = Image.open(file_path)
#
# plt.imshow(image)
#
# plt.show()
