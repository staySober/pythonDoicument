#!/usr/bin/env python
#coding=utf-8
import json
import werkzeug
from flask import Flask,jsonify,request
data = {'sober':{'age':24,'sex':'女'},
        'kevin':{'age':12,'sex':'男'}
        }
err = {'sober':404,
       'kevin':502
       }
app = Flask(__name__)#创建一个服务，赋值给APP

class PostAndGet:
    @app.route('/getInfo',methods=['post','get'])#指定接口访问的路径，支持什么请求方式get，post
    #请求后直接拼接入参方式
    def getInfo():
        if request.method == 'POST':
            username = request.form.get('username','')
        else:
            username = request.args.get('username')#使用request.args.get方式获取拼接的入参数据
        
        if username in data:  # 判断请求传入的参数是否在字典里
            return str(data[username]).encode('utf-8')
        #如果在的话，则返回data对应key的值转成的json串信息
        else:
            return '<h1>404NOTFOUND</h1>'
    #如果不在的话，返回err对应key的value转成的json串信息    
    
    @app.route('/setInfo',methods = ['psot','get'])
    def setInfo():
           username = request.args.get('username')
           value = request.args.get('userInfoJson')
           data[username] = value;
           return str('插入成功').encode('utf-8')

    @app.route('/uploadFile', methods =['post'])
    def uploadFile():
        if request.method == 'POST':
            file = request.files['uploadFile']
            file.save('/usr/local', + secure_filename(file.filename))
        return 'upload success'

app.run(host='0.0.0.0',port=8803,debug=True)
#这个host：windows就一个网卡，可以不写，而liux有多个网卡，写成0:0:0可以接受任意网卡信息
#通过访问127.0.0.1:8802/get_user，form—data里输入username参数，则可看到返回信息