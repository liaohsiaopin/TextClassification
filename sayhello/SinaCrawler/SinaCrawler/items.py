# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinacrawlerItem(scrapy.Item):
    #新闻标题
    title=scrapy.Field()
    #新闻内容
    content=scrapy.Field()
    #新闻链接
    url=scrapy.Field()
    #文件存储路径
    filePath=scrapy.Field()
