# -*- coding:utf-8 -*-
# 创建表，插入数据
def createtable():
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        # 需要在自己的MySQl数据库中创建一个名为auth的库
        database='auth',
        charset='utf8'
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql1 = """
        -- 创建表
        create table userinfo(id int primary key auto_increment,username char(20) not null unique,password char(20) not null);
    """
    sql2 = """
       -- 插入数据
        insert into userinfo(username,password) values('whw','123'),('www','666');
    """
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    createtable()
