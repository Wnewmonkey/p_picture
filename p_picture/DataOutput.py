import os

from bs4 import BeautifulSoup

from 爬图片.UrlManager import UrlManager
from 爬图片.HtmlDownloader import HtmlDownloader
#数据存储器
class DataOutput(object):
    def __init__(self):
        self.downloader = HtmlDownloader()

        self.manager = UrlManager()

    def urldown(self,url,name):
        if url is None:
            return
        html = self.downloader.download(url)
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        link = soup.find('img', attrs={'id': 'bigImg'})

        if not os.path.exists(name):
            with open(name, 'wb') as f:
                img = self.downloader.download(str(link)[42:148])
                f.write(img)
        else:
            return




