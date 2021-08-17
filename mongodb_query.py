#-*- coding: UTF-8 -*-
# @Time    : 2021-8-17 16:02:34
# @Author  : 费海瑞
# @File    : mongodb_query.py
# @Software: PyCharm

import pymongo

mongo = pymongo.MongoClient(host='127.0.0.1', port=27017, tz_aware=True)

'''
  必须是连接通过方法获取到数据库
  数据库通过方法获取到集合
  敲代码就会有提示功能
'''
# 获取集合
db = mongo.get_database('sxt')
col =  db.get_collection('col')

# 查询所有
def show(r):
    """展示所有文档"""
    for i in r:
        print(i)

# and操作
def test_and():
    r = db.col.find({
        "$and":[
            {"_id":{"$gt":3,"$lt":5}},
            {"age":{"$lte":21}}
        ]
    })
    show(r)

# or操作
def test_or():
    r = db.col.find({
        "$or":[
            {"_id":{"$gt":3,"$lt":5}},
            {"age":{"$lte":21}}
        ]
    })
    show(r)

# 正则操作
def test_regex():
    # 模糊查询
    # r = col.find({'name':{"$regex":'^z.*?(n|u)$'}})
    # show(r)
    r =col.find({'name':{'$regex':'qi$'}})
    print('liek %qi')
    show(r)


# 投影
def test_project():
    r = col.find({
        "name":{"$regex":'^z.*?(n|u)$'}
    },
        {
            "_id":0,
            "name":1,
            "age":1
        }
    )
    show(r)


# 数组
def test_array():
    r = col.find(
        {},
        {
            "_id": 0,
            "name": 0,
            "age": 0,
            "hobbies":{"$slice":[0,2]},
        }
    )
    show(r)


# 排序
def test_sort():
    # 按姓名正序
    # r = col.find({},{"name":1}).sort("name",pymongo.ASCENDING)
    # show(r)
    # 按年龄到序 按id正序
    r = col.find({},{"age":-1,"_id":1}).sort([("age",pymongo.DESCENDING),("_id",pymongo.ASCENDING)])
    show(r)


# 分页
def test_age(pageSize,pageNum):
    r = col.find().limit(pageSize).skip((pageNum-1)*pageSize)
    show(r)


# 分组
def test_group():
    # r = col.aggregate([{"$match":{"age":21}}])
    r = col.aggregate([{"$group": {"_id": "$age"}}])
    show(r)



if __name__ == '__main__':
    # show(comment.find())
    # test_and()
    # test_or()
    # test_regex()
    # test_project()
    # test_array()
    # test_sort()
    # test_age(2,1)  # 1页两条数据
    test_group()