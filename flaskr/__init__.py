#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        flask-tutorial
# Purpose:
#
# Author:      zhao.jingqing
#
# Created:     2018/6/14 14:03
# Copyright:   (c) zhao.jingqing 2018
# Licence:     <your licence>
# IDE:         PyCharm
#-------------------------------------------------------------------------------

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
def main():
    pass


if __name__ == '__main__':
    main()