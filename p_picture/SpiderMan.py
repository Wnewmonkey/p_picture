
#爬虫调度器
import os

from 爬图片.HtmlParser import HtmlParser
from 爬图片.DataOutput import DataOutput
from 爬图片.HtmlDownloader import HtmlDownloader
from 爬图片.UrlManager import UrlManager

class SpiderMan(object):

#--------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.parser = HtmlParser()
        self.output = DataOutput()
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()

#--------------------------------------------------------------------------------------------------------------
    def crawl(self,root_url):

        #把主页的地址放在未爬去的列表中
        pages = input("请输入需要获取的页数：")
        for page in range(1,int(pages)+1):
            page_url = root_url[:48] + "_" + str(page) + root_url[48:]
            self.manager.add_new_root_url(page_url)


        #创建根目录
        folder = '壁纸'
        if not os.path.exists(folder):
            # 创建文件夹
            os.mkdir(folder)
            # 改变当前工作目录到此文件夹
            os.chdir(folder)
        else:
            # 改变当前工作目录到此文件夹
            os.chdir(folder)
        root_addr = os.getcwd()


        #将图集地址以及图集名称放入的列表中
        while self.manager.has_new_root_url():
            #从URL管理器中获取新的url
            new_root_url = self.manager.get_new_root_url()
            #HTML下载器下载网页
            html = self.downloader.download(new_root_url)
            #HTML解析器抽取网页数据,得到图集的URL以及图片的URL
            self.manager.new_middle_urls,self.manager.names=self.parser.get_new_middle_urls(new_root_url,html)

        #将图片地址放入列表中，并创建图集文件夹
        while self.manager.has_new_middle_url():
            name = self.manager.get_name()
            if not os.path.exists(name):
                # 创建文件夹
                os.mkdir(name)
                # 改变当前工作目录到此文件夹
                os.chdir(name)
                print('正在下载'+name)
            else:
                # 改变当前工作目录到此文件夹
                os.chdir(name)
            new_middle_url = self.manager.get_new_middle_url()
            print('图集地址：'+new_middle_url)
            self.manager.add_new_top_url(self.parser.get_new_top_urls(new_middle_url))

            #下载图片
            i=1
            while self.manager.has_new_top_url():
                new_top_url = self.manager.get_new_top_url()
                self.output.urldown(new_top_url,name+'_'+str(i)+'.jpg')
                i+=1
            print(name+'下载完毕')
            os.chdir(root_addr)
        exit()


#--------------------------------------------------------------------------------------------------------------
if __name__ =='__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://sj.zol.com.cn/apple/iphone7_bizhi/comment.html")
    #搜索功能
