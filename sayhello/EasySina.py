import requests
from bs4 import BeautifulSoup

#根据页面链接获取文本

class EasySina:
    def getUrlContent(self,inputUrl):
        target = inputUrl  # 目标网址
        print("终于到了这一步")
        #get方法
        req = requests.get(target)  # 获取对象
        req.encoding = "utf-8"  # 设置编码格式
        html = req.text  # 获得网页源代码
        soup = BeautifulSoup(html, 'lxml')  # 利用BeautifulSoup进行解析
        #获取内容
        article=[]
        for p in soup.select('.article p')[:-1]:
            article.append(p.text.strip())
        print(article)
        return ''.join(article)
