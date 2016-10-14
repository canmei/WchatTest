'''
Created on Oct 13, 2016

@author: xhuiton
'''
# -*-coding:utf-8-*-
import web
from handle import Handle

urls = (
        '/wx','Handle',
)

if __name__ == '__main__':
    app = web.application(urls,globals())
    app.run()