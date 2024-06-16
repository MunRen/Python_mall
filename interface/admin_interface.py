#!/usr/bin/python3

'''
管理员相关接口
'''

from db import db_handler
from lib import common

logger = common.get_logger('admin')

# 冻结账户接口
def lock_user_interface(username):
    # 1.拿到用户数据
    user_data = db_handler.select_data(username)

    # 2.判断用户是否存在
    if not user_data:
        return False, f'\n用户：{username} 不存在！'

    if user_data.get('locked'):
        user_data['locked'] = False
        db_handler.save(user_data)
        msg = f'用户：{username} 已解冻'
        logger.info(msg)
        return True, msg

    user_data['locked'] = True
    db_handler.save(user_data)
    msg = f'用户：{username} 已冻结'
    logger.warning(msg)
    return True, msg
