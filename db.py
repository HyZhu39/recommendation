# -*- coding: UTF-8 -*-

import pymysql
import traceback

# 打开数据库连接
db = pymysql.connect(host='localhost',user='root',passwd='ascent',db='today',port=3306,charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM users"
sql2 = "SELECT * FROM orders"
sql3 = "SELECT * FROM dishes"



#['user_id', 'gender', 'age', 'occupation', 'zip']#设列名称
#['user_id', 'movie_id', 'rating', 'timestamp']
#['movie_id', 'title', 'genres']

with open('data\\users.dat', 'w', encoding='utf-8') as f:
    # 数据库读取的特点是每读一次会把前一次的盖掉
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            userid = row[0]
            gender = row[5]
            age = row[6]
            occupation = row[8]
            zip = row[9]
            # 打印结果
            f.write(str(userid) + "::" + str(gender) + "::" + str(age) + "::" + str(occupation) + "::" + str(zip)+"\n")
            print("userid=%s,gender=%s,age=%s,occupation=%s,zip=%s" % \
                  (userid, gender, age, occupation, zip))
    except:
        print("Error: unable to fetch data")
        msg = traceback.format_exc()  # 方式1
        print(msg)



with open('data\\ratings.dat', 'w', encoding='utf-8') as f2:
    try:
        # 执行SQL语句
        cursor.execute(sql2)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            userid = row[1]
            movieid = row[5]
            rating = row[4]
            timestamp = row[3]
            # 打印结果
            f2.write(str(userid)+"::"+str(movieid)+"::"+str(rating)+"::"+str(timestamp)+"\n")
            print("userid=%s,movieid=%s,rating=%s,timestamp=%s" % \
                  (userid, movieid, rating, timestamp))
    except:
        print("Error: unable to fecth data")

with open('data\\movies.dat', 'w', encoding='utf-8') as f3:
    try:
        # 执行SQL语句
        cursor.execute(sql3)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            movieid = row[0]
            title = row[2]
            genres = row[5]
            # 打印结果
            f3.write(str(movieid)+"::"+str(title)+"::"+str(genres)+"\n")
            print("movieid=%s,title=%s,genres=%s" % \
                  (movieid, title, genres))
    except:
        print("Error: unable to fecth data")

# 关闭数据库连接
db.close()