#-*- coding: UTF-8 -*-
# @Time    : 2021-8-17 11:48:29
# @Author  : 费海瑞
# @File    : mongodb_test.py
# @Software: PyCharm

import pymongo
from pymysql import Date

# 连接数据库
mongo = pymongo.MongoClient(host='127.0.0.1', port=27017, tz_aware=True)

def handler_db():
    """操作数据库"""
    # 创建或者选择数据库
    db = mongo.sxt

    # 删除数据库
    mongo.drop_database(db)

    # 获取数据库
    mongo.list_database_names()


def handler_collection():
    """操作集合"""
    # 获取数据库
    db = mongo.sxt

    # 创建或者选择集合
    col = db.create_collection('col')
    print('创建集合:',col)

    # 获取一个集合
    col =db.col
    print('获取集合:', col)
    print('获取所有集合:', db.list_collection_names())
    print('获取所有集合对象:', db.list_collections())

    # 删除集合
    print(db.drop_collection('col'))


def handler_document():
    """操作文档"""
    # 获取集合
    col = mongo.sxt.col

    # 添加数据
    # 1、插入单条数据
    # col.insert({"_id":1,"name":"zhangsan","age":18})
    # col.insert_one({"_id":2,"name": "lisi", "age": 20})
    # 2、插入多条数据
    user1 = {"_id":4,"name":"liqi","age":21}
    user2 = {"_id":5, "name": "zhaoba", "age": 22}
    col.insert_many([user1,user2])

    # 更改数据
    # user = {"name":"tianqi","age":23}
    # upt = col.update_one(filter={"name":"zhaoliu"},update={"$set":user})

    # 删除数据
    # 1、删除单条
    # d = col.delete_one({"name":"tianqi"})
    # print(d)
    # 2、删除多条
    # d = col.delete_many({'name':'老李'})


def handler_index():
    """操作索引"""
    # 获取数据库
    db = mongo.sxt

    # 创建索引 默认正序 名字默认是属性1
    # i = db.col.create_index('_id')
    # print(i)

    # 创建索引 添加排序规则
    # i = db.col.create_index([('age',pymongo.DESCENDING)])

    # 删除索引
    print(db.col.drop_index('_id'))    # 注：如果索引不存在，就会报错
    # 删除所有索引
    print(db.col.drop_indexes())


if __name__ == '__main__':
    # handler_db()
    # handler_collection()
    # handler_index()
    handler_document()