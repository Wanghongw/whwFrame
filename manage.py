# -*- coding:utf-8 -*-
from urls import urlpatterns
from wsgiref.simple_server import make_server


#这个文件里面是框架的主体内容
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    for url_tuple in urlpatterns:
        if url_tuple[0] == path:
            data = url_tuple[1](environ) #environ要传进去，因为处理逻辑里面可能要用
            break
        else:
            data = b'sorry 404!,not found the page'
    return [data]
        # 注意，我们如果直接返回中文，没有给浏览器指定编码格式，所以我们需要gbk来编码一下，浏览器才能识别
        # data='登陆成功！'.encode('gbk')


httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()


