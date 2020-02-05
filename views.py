# -*- coding:utf-8 -*-
import datetime
from urllib.parse import parse_qs

from utils import webAuth

# 返回登陆页面
def login(environ):
    with open('templates/web.html', 'rb') as f:
        data = f.read()
    return data

# 用户认证
def auth(environ):
    # 登陆认证
    # 1.获取用户输入的用户名和密码
    # 2.去数据库做数据的校验，查看用户提交的是否合法
    # form表单使用post方式提交
    if environ.get("REQUEST_METHOD") == "POST":
        # 获取请求体数据的长度,因为提交过来的数据需要用它来提取
        # 注意POST请求和GET请求的获取数据的方式不同！
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        # POST请求获取数据的方式
        request_data = environ['wsgi.input'].read(request_body_size)
        print('>>>>>', request_data)  # b'username=whw&password=123'，是个bytes类型数据！
        # 注意将bytes转换为str
        request_data = str(request_data,encoding="utf-8")
        # parse_qs可以帮我们解析数据
        re_data = parse_qs(request_data)
        print('拆解后的数据', re_data)  # {'password': ['123'], 'username': ['whw']}
        # 处理拆解后的数据
        data = webAuth.handle_data(re_data)
    # form表单使用get方式提交
    elif environ.get("REQUEST_METHOD") == "GET":
        # GET请求获取数据的方式，只能按照这种方式取
        print('QUERY_STRING:', environ['QUERY_STRING'])  # username=whw&password=123,是个字符串类型数据
        request_data = environ['QUERY_STRING']
        # parse_qs可以帮我们解析数据
        re_data = parse_qs(request_data)
        print('拆解后的数据', re_data)  # 拆解后的数据 {'password': ['123'], 'username': ['whw']}
        # 处理拆解后的数据
        data = webAuth.handle_data(re_data)
    else:
        data = b"wrong request method!"
    return data

# ico
def favicon(environ):
    with open('whw.ico','rb') as f:
        data = f.read()
    return data

# 主页
def index(environ):
    with open('templates/index.html','rb') as f:
        data = f.read()
    return data

#查看当前时间的
def timer(environ):
    data = str(datetime.datetime.now()).encode('utf-8')
    return data

