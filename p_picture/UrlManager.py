
#Url管理器
class UrlManager(object):

# -----------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.new_root_urls = []     #未爬去的主页的URL列表
        self.old_root_urls = []     #已爬取的主页的URL列表
        self.new_middle_urls = []   #未爬去的图集URL列表
        self.old_middle_urls = []   #已爬去的图集URL列表
        self.new_top_urls = []      #未爬取的图片URL列表
        self.old_top_urls = []      #已爬取的图片URL列表
        self.names = []

#--------------------------------------------------------------------------------------------------------------

    def add_new_root_url(self,url):
        '''
        将新的URL添加到未爬去的URL列表中
        :param url: 单个URL
        :return:
        '''
        if url is None:
            return
        if url not in self.new_root_urls and url not in self.old_root_urls:
            self.new_root_urls.append(url)

#--------------------------------------------------------------------------------------------------------------
    def get_new_root_url(self):
        '''
        获取一个未爬取的主页URL
        :return:
        '''
        new_root_url = self.new_root_urls.pop(0)
        self.old_root_urls.append(new_root_url)
        return new_root_url
#--------------------------------------------------------------------------------------------------------------

    def add_new_middle_url(self,url):
        '''
        将新的URL添加到未爬去的URL列表中
        :param url: 单个URL
        :return:
        '''
        if url is None:
            return
        if url not in self.new_middle_urls and url not in self.old_middle_urls:
            self.new_middle_urls.append(url)
#--------------------------------------------------------------------------------------------------------------
    def get_new_middle_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_middle_url = self.new_middle_urls.pop(0)
        self.old_middle_urls.append(new_middle_url)
        return new_middle_url

#--------------------------------------------------------------------------------------------------------------

    def add_new_top_url(self,url):
        '''
        将新的URL添加到未爬去的URL列表中
        :param url: 单个URL
        :return:
        '''
        if url is None:
            return
        if url not in self.new_top_urls and url not in self.old_top_urls:
            self.new_top_urls.append(url)
#--------------------------------------------------------------------------------------------------------------
    def get_new_top_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_top_url = self.new_top_urls[0].pop(0)
        self.old_top_urls.append(new_top_url)
        return new_top_url







#--------------------------------------------------------------------------------------------------------------


    def has_new_root_url(self):
        '''
        判断是否有未爬取的主页URL
        :return:
        '''
        return self.new_root_url_size()!=0
#--------------------------------------------------------------------------------------------------------------
    def new_root_url_size(self):
        '''
        获取未爬取的主页URL列表大小
        :return:
        '''
        return len(self.new_root_urls)
#--------------------------------------------------------------------------------------------------------------


    def has_new_middle_url(self):
        '''
        判断是否有未爬取的图集URL
        :return:
        '''
        return self.new_middle_url_size()!=0
#--------------------------------------------------------------------------------------------------------------
    def new_middle_url_size(self):
        '''
        获取未爬取的图集URL列表大小
        :return:
        '''
        return len(self.new_middle_urls)
#--------------------------------------------------------------------------------------------------------------


    def has_new_top_url(self):
        '''
        判断是否有未爬取的图集URL
        :return:
        '''
        return self.new_top_url_size()!=0
#--------------------------------------------------------------------------------------------------------------
    def new_top_url_size(self):
        '''
        获取未爬取的图集URL列表大小
        :return:
        '''
        return len(self.new_top_urls[0])
#--------------------------------------------------------------------------------------------------------------
    def add_name(self,name):

        if name is None:
            return
        if name not in self.names:
            self.names.append(name)
#--------------------------------------------------------------------------------------------------------------
    def get_name(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        name = self.names.pop(0)
        return name
