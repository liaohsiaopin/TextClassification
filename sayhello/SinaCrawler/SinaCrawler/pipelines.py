# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class SinacrawlerPipeline(object):
    wb=Workbook()
    ws=wb.active

    def process_item(self, item, spider):
        print(item['content'])
        line=["房产",item['content']]
        self.ws.append(line)
        self.wb.save('home.xlsx')
        # wb = xlwt.Workbook("encoding ='utf8'")
        # ws = wb.add_sheet("business")
        # ws.write(count,0,content)
        # print('c')
        # ws.write(count,1,'财经')
        # print('d')
        # self.addCount()
        # print(count)
        # wb.save('test1.xls')

