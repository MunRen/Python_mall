#!/usr/bin/python3

'''
公共方法
'''
import logging.config
from conf import settings


# 登陆认证装饰器
def login_auth(func):
    def wrapper(*args, **kwargs):
        from core import src
        if src.logged_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('\n登陆后操作！')
            src.login()
    return wrapper

def pwd_to_sha256(password):
    import hashlib
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    sha.update('接着奏乐接着舞'.encode('gbk'))
    return sha.hexdigest()


# 日志记录功能
def get_logger(logger_name):
    # 1.加载日志配置文件
    logging.config.dictConfig(settings.LOGGING_DIC)

    # 2.获取logger
    logger = logging.getLogger(logger_name)
    return logger