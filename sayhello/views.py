# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template

from sayhello import app
from sayhello.forms import HelloForm
from sayhello.EasySina import EasySina
from sayhello.TextClassification.predict import CnnModel
from sayhello.SinaCrawler.SinaCrawler.spiders.sina import SinaSpider
import requests

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        #单击获取内容按钮
        if form.submit.data:
            url = form.url.data
            p=EasySina()
            form.text.data=   p.getUrlContent(url)

        #单击文本分类按钮：
        if form.submit2.data:
            #获取文本内容
            content=form.text.data
            #分类
            cnn=CnnModel()
            form.classification.data=cnn.predict(content)
            print(cnn.predict(content))
            print("以上是分类结果")
            #预测

        #重定向，是index的url /
        return render_template('index.html', form=form)
        return redirect(url_for('index'))

    #render_template的功能是对先引入index.html，同时根据后面传入的参数，对html进行修改渲染。
    return render_template('index.html', form=form)

  #  return render_template('index.html', form=form, messages=messages)
