# -*- coding: utf-8 -*-
# @FileName: StuSystem.py
# @Author  : zzy
# @Time    : 2021/2/1 11:00
# @Software: PyCharm
def main():
    while True:
        menu()
        choose = int(input('请选择'))
        if choose in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choose == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break  # 退出系统
                else:
                    continue
            elif choose == 1:
                insert()
            elif choose == 2:
                search()
            elif choose == 3:
                delete()
            elif choose == 4:
                modify()
            elif choose == 5:
                sort()
            elif choose == 6:
                total()
            elif choose == 7:
                show()


def menu():
    print('==================================学生信息管理系统==================================')
    print('-------------------------------------功能菜单-------------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t\t7.现实所有学生能够信息')
    print('\t\t\t\t\t\t0.退出')
    print('---------------------------------------------------------------------------------')

def insert():
    pass


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__=='__main__':
    main()