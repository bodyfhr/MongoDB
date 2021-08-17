#-*- coding: UTF-8 -*-
# @Time    : 2021-8-17 11:37:57
# @Author  : 费海瑞
# @File    : mongodb_init.py
# @Software: PyCharm

import pymongo # 导入pymongo模块

# 第一种方法连接
def mongodb_init01():
    """连接数据库"""
    mongo = pymongo.MongoClient(host='127.0.0.1',port=27017,tz_aware=True)
    rows = mongo.articledb.comment.find()
    for r in rows:
        print(r)


# 第二种方法连接
def mongodb_init02():
    """连接数据库"""
    uri = "mongodb://{}:{}".format('127.0.0.1',27017)
    mongo = pymongo.MongoClient(uri,tz_aware=True)


if __name__ == '__main__':
    # mongodb_init01()
    mongodb_init02()