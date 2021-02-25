# # -*- coding: utf-8 -*-
# # @FileName: demo.py
# # @Author  : zzy
# # @Time    : 2021/1/29 10:44
# # @Software: PyCharm
#
# # import keyword
# # from decimal import Decimal
# #
# # print(keyword.kwlist)
# #
# # name = 'qer'
# # print('标识', id(name))
# # print('名字', type(name))
# # print('erjinzhi', 0b101010011001)
# #
# # print(Decimal('1.1')+Decimal('2.2'))
# #
# # b1 = True
# # print(b1+1)
# #
# #
# # money = int(input('输入'))
# # if money % 2 == 0:
# #     print('偶数')
# # else:
# #     print('奇数')
# #
# # a = 1
# # while a < 10:
# #     print(a)
# #     a += 1
# # sum = 0
# # for b in range(1, 100):
# #     if b % 2 == 0:
# #         sum += b
# # print(sum)
# # lis = ['hello', 'world', 98, 'hello', 10, 20, 30, 20, 49]
# # print(lis[1])
# # print(id(lis))
# # lis2 = lis[1:5]
# #
# # print(id(lis2))
# # print(lis)
# # lis[1:4]
# # print(lis)
# # print(id(lis))
# # a=[1,23,45,5,7,7,5,5,8,9,5,3,46,6,74,23,567,6567,234,67,57]
# # print(a)
# # # for b in a:
# # #     print(b)
# # print(id(a))
# # a.sort()
# # print(a)
# # print(id(a))
# #
# # a.sort(reverse=True)
# # print(a)
# # print(id(a))
# # a={'张三':100,'李四':200}
# # print(a)
# # student=dict(name='jack',age=20)
# # print(student)
# # d={}
# # print(d)
# # print(student.get('name'))
# # print(student.keys())
# # print(student.values())
# # keys=student.keys()
# # values=student.values()
# # print(keys)
# # print(type(keys))
# # print(list(keys))
# # print(values)
# # print(type(values))
# # print(list(values))
# #
# # items=student.items()
# # print(items)
# # print(type(items))
# # print(list(items))
# # a={'张三':100,'李四':200}
# # for item in a:
# #     print(item,a[item],a.get(item))
# # student=dict(name='jack',age=20)
# # for item in student:
# #     print(item, student[item], student.get(item))
#
# # '''可变序列 列表，字典'''
# # lst=[10,20,30]
# # print(id(lst))
# # lst.append(40)
# # print(id(lst))
# # '''不可变序列 字符串，元组'''
# # s='hello'
# # print(id(s))
# # s=s+'world'
# # print(id(s))
# # print(s)
#
# # ''''''
# # t=('python','hello',90)
# # print(t)
# # print(type(t))
# #
# #
# # t1=tuple(('python','hello',90))
# # print(t1)
# # print(type(t1))
#
# '''集合'''
# '''不允许重复'''
# s={1,2,3,4,5,6,6,7,8,8,9,0,12,14,345,34,53,56,36,6,5,635,67,367,65}
# print(s)
# print((s,type(s)))
#
# s1=set(range(10))
# print((s1,type(s1)))
#
# s2=set([1,2,3,4,5,6,7,8,9,0,123,134,43,5,4,634,6])
# print(s2,type(s2))
# def test (taaaa):
#     print(taaaa)
#     return
# test("efe4f34g3g")
# def fib(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# for i in range(1,20):
#     print(fib(i),end=" ")

try:
    n1 = int(input('请输入一个整数'))
    n2 = int(input('请输入第二个整数'))
    resault = n1/n2
    print('结果为',resault)
except:
    ZeroDivisionError

