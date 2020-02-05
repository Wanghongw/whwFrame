# -*- coding:utf-8 -*-
# 对用户名和密码进行验证
def auth(username,password):
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        database='auth',
        charset='utf8'
    )
    print('userinfo',username,password)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from userinfo where username=%s and password=%s;'
    res = cursor.execute(sql, [username, password])
    if res:
        return True
    else:
        return False

# 处理拆解后的数据
def handle_data(re_data):
    username = re_data['username'][0]
    password = re_data['password'][0]
    print(username, password)
    # 进行验证：
    status = auth(username, password)
    if status:
        # 3.将相应内容返回
        with open('templates/webSuccess.html', 'rb') as f:
            data = f.read()
    else:
        data = b'auth error'
    return data