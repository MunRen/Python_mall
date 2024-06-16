#!/usr/bin/python3

"""
管理员视图层
"""
from core import src
from interface import admin_interface

# 添加账户功能
def add_user():
    is_admin = input('是否添加管理员(y or n)：').strip().lower()
    if is_admin == 'y':
        src.register(True)
    else:
        src.register()

# 冻结账户功能
def lock_user():
    while True:
        # 1.接受管理员输入的用户名
        lock_username = input('请输入需要冻结的用户名：').strip()
        is_lock = input('按任意键确认/n退出：').strip().lower()

        # 2. 判断输入的用户名是否是admin用户
        if src.logged_user == lock_username:
            print('不可冻结自己')
            break

        # 3.判断是否想要退出
        if is_lock == 'n':
            break

        # 4.调用冻结账户的接口层冻结账户
        flag, msg = admin_interface.lock_user_interface(lock_username)
        print(msg)
        if flag:
            break
# 给用户充值
def recharge_to_user():
    username = input('请输入需要充值的用户名：').strip()
    src.recharge(username)

func_dic = {
    '0': ('返回首页',),
    '1': ('添加账户', add_user),
    '2': ('冻结账户', lock_user),
    '3': ('给用户充值', recharge_to_user)
}



# 管理员视图层主程序
def main():
    while True:
        print('管理员功能'.center(20, '='))
        for num in func_dic:
            print(f'{num} {func_dic.get(num)[0]}'.center(20, ' '))
        print('我是有底线的'.center(20, '='))
        opt = input('请输入功能编号：').strip()
        if opt not in func_dic:
            print('此功能不存在请重新输入')
            continue
        if int(opt) == 0:
            break
        func_dic.get(opt)[1]()