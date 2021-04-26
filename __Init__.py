'''
Author: fanjia
LastEditors: fanjia
Date: 2021-04-26 18:45:52
LastEditTime: 2021-04-26 18:46:06
Description: 
FilePath: /flask-learning/templates/__Init__.py
'''
from flask import Flask

app = Flask('flask-learning')

@app.route('/')
def index():
    return 'index'