from 爬图片.UrlManager import UrlManager
from 爬图片.HtmlDownloader import HtmlDownloader
from bs4 import BeautifulSoup
#Html解析器
class HtmlParser(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()


#——————————————————————————————————————————————————————————————————————————————————————————————————————————
#将每页的图集地址存入列表
    def get_new_middle_urls(self, new_root_url,html):
        '''
        抽取下载页面的图集地址
        :param page_url: 下载页面的URL
        :param soup:   soup
        :return:    返回图集的url列表
        '''
        if new_root_url is None or html is None:
            return
        soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        links = soup.find_all('a',attrs={'class':'pic'})
        for each in links[0:15]:
            id = 'http://sj.zol.com.cn'+each.get('href')
            self.manager.add_name(each.get('title'))
            self.manager.add_new_middle_url(id)
        return self.manager.new_middle_urls,self.manager.names

#——————————————————————————————————————————————————————————————————————————————————————————————————————————

    def get_new_top_urls(self,new_middle_url):

        self._get_next(new_middle_url)
        return self.manager.new_top_urls




#——————————————————————————————————————————————————————————————————————————————————————————————————————————
    def _get_next(self,html):
        if html not in self.manager.new_top_urls and html not in self.manager.old_top_urls:
            self.manager.add_new_top_url(html)
        else:
            return

        htm = self.downloader.download(html)
        soup = BeautifulSoup(htm, 'html.parser', from_encoding='utf-8')
        b = 'http://sj.zol.com.cn' + soup.find('a', attrs={'class': 'next'}).get('href')
        self._get_next(b)






