# _*_coding:utf-8 _*_

# a = "你好"
# b = a.encode(encoding='utf-8')
# c = b.decode()
# print(c)

#
# def func():
#     global x
#     x = 2
#     print 'x is', x
#
#     print 'Changed local x to', x
#
# def test():
#     print(x)
#
# test()
# print 'Value of x is', x
# import os
# from app01 import models
# import conf

# os.environ['DJANGO_SETTINGS_MODULE'] = 'svnmanager.settings'     #s12day16 是你的setting所在的项目名
# import django
# django.setup()
#
# confdic = conf.configure()
# cc = confdic['readyhost']
# print(cc)
# models.hosts.objects.filter(host_w_ip=cc)



try:
    a=1
    c="kk"
    d = a+c
    print(d)
except:
    a = 1
    b = 2
    d = a+b
    print(d)