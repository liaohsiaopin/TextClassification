# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    url = TextAreaField('请输入新闻网址：', validators=[Length(0, 300)])
    submit = SubmitField('获取内容')
    text = TextAreaField('待分类新闻文本：', validators=[Length(0, 50000)])
    submit2 = SubmitField('文本分类')
    classification = StringField('分类结果：', validators=[Length(0, 20)])

