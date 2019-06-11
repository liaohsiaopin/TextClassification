# -*- coding: utf-8 -*-
import scrapy
from sayhello.SinaCrawler.SinaCrawler.items import SinacrawlerItem

global count
count=0


class SinaSpider(scrapy.Spider):
    name = 'sina'
    '''
    财经类
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/']
    
    体育类
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/']
    
    科技类
    allowed_domains = ['tech.sina.com.cn']
    start_urls = ['http://tech.sina.com.cn/']
    start_urls = ['http://5g.sina.com.cn/']
    start_urls = ['http://tech.sina.com.cn/notebook']
    start_urls = ['http://tech.sina.com.cn/internet/']
    
    教育类
    allowed_domains = ['edu.sina.com.cn']
    start_urls = ['http://edu.sina.com.cn/']
    start_urls = ['http://edu.sina.com.cn/gaokao']
    
    时尚类
    allowed_domains = ['fashion.sina.com.cn']
    start_urls = ['http://fashion.sina.com.cn/']
    start_urls = ['http://fashion.sina.com.cn/luxury']
    
    游戏类
    allowed_domains = ['games.sina.com.cn']
    start_urls = ['http://games.sina.com.cn']
    start_urls = ['http://games.sina.com.cn/pc']
    
    娱乐类
    allowed_domains = ['ent.sina.com.cn/']
    start_urls = ['http://ent.sina.com.cn']
    
    房产类
    allowed_domains = ['bj.leju.com/']
    start_urls = ['bj.leju.com/news/']
    
    时政类
    allowed_domains = ['news.sina.com.cn/']
    start_urls = ['http://news.sina.com.cn']
        start_urls = ['https://news.sina.com.cn/world']
    加入了dont_filters=True 
    
    汽车类  需要查看JavaScript
    allowed_domains = ['auto.sina.com.cn/']
    start_urls = ['https://auto.sina.com.cn/']
    
    家居类 搜狐 失败了 反爬
    allowed_domains = ['jiaju.sina.com.cn/']
    start_urls = ['https://jiaju.sina.com.cn/']
    
    '''
    allowed_domains = ['auto.sina.com.cn/']
    start_urls = ['https://auto.sina.com.cn/']

    def addCount(self):
        global count
        count = count+1

    def parse(self, response):
        #news=response.xpath('//*[@id="directAd_huaxia"]/div[2]/div[3]')
        urls=response.xpath('//a/@href').extract()
        for i in range(len(urls)):
            #是否以finance为开头
       #     print(urls[i])
            #sohu以html结尾 sina以shtml结尾
            if_belongs=((urls[i].startswith('https://house.focus.cn/zixun') or urls[i].startswith('http://house.focus.cn/zixun'))and urls[i].endswith('html'))
            if(if_belongs):
                if('2019' in urls[i] or '2018' in urls[i] or '2017' in urls[i] or '2016' in urls[i] ):
                    print(urls[i])
                    yield scrapy.Request(url=urls[i],callback=self.detail_parse, dont_filter=True)

    def detail_parse(self,response):
        item=SinacrawlerItem()
        content=""
        print("try it")
        #news id=article  others id=artibody  家居：articleText
       # content_list = response.xpath('//div[@id=\"articleText\"]/p/text()').extract()
        content_list = response.xpath('// *[ @ id = "artibody"] /p/text()').extract()
        #搜狐新闻
       # content_list = response.xpath('//div[@id=\"info-content\"]/p/text()').extract()
        for i in content_list:
            content+=i
        content = content.replace('\u3000', '')
        print(content)
        item['content']=content
        yield item

#获取URL，并调用get_Content获取网页内容
    def get_url(self,inputUrl):
        print("get it")
        url=inputUrl
        print(url)
        yield scrapy.Request(url=url,callback=self.get_Content,dont_filter=True)

    def get_Content(self,response):
        print("Here I am")
        content=''
        content_list = response.xpath('// *[ @ id = "artibody"] /p/text()').extract()
        for i in content_list:
            content += i
        content = content.replace('\u3000', '')
        print(content)








