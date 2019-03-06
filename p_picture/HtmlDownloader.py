import urllib.request
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            print('fdsafasdfasd')
            return None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        # 判断访问页面是否存在，如果存在返回页面数据，如果不存在返回0
        try:
            # 创建一个req对象，把url传进去,加入header,伪装成浏览器访问页面
            req = urllib.request.Request(url=url, headers=headers)
            html = urllib.request.urlopen(req).read()
        # 如果返回错误为404，返回0
        except urllib.error.HTTPError as e:
            if e.code !=200:
                return None
        return html



