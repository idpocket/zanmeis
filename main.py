import requests
from lxml import etree
import time
class ZanMei(object):

    def __init__(self):
        self.header ={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Referer': 'https://www.zanmeis.com/gepu/s/time_all_all_all_all.htm',
            'Cookie':'SL_G_WPT_TO=zh-CN; Hm_lvt_cf70645f4477d0d04da2e557841a158e=1642737354; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _ga=GA1.2.661394252.1642737354; _gid=GA1.2.1056289505.1642737355; __gads=ID=521ead2b7c548e9b-22de1b6b08d0007b:T=1642737354:RT=1642737354:S=ALNI_MZelcLcxAZhppOKFfklCovuL_ETuQ; Hm_lpvt_cf70645f4477d0d04da2e557841a158e=1642739448'
        }


    def parse_html(self,i=None):

        url = f'https://www.zanmeis.com/gepu/{i}.htm'
        try:
            r = requests.get(url=url,headers=self.header)

            html = etree.HTML(r.text)

            title = html.xpath('''//*[@id="view"]/div[2]/div[2]/div/div/div[1]/h3/text()''')
            imgurl = html.xpath('''//*[@id="view"]/div[2]/div[3]/div[1]/div/a/@href''')
            return title[0],imgurl[0]
        except:
            print('页面解析错误')

    def contentsAndtitle(self,url):
        try:
            r = requests.get(url=url, headers=self.header)
            img = r.content
            return img
        except:
            print(f'图片url解析失败')

    def download(self,title,content):
        try:
            path = f'./image/{title}.jpg'
            with open(path,'wb') as f:
                f.write(content)
            print(f'{title},保存成功')
        except:
            print(f'{title}下载失败')
    def isurl(self,url):
        path = './urls.txt'
        with open(path, 'r') as f:
            s = f.read()
            if url in s:

                return False
            else:
                return True
    def wisurl(self,url):
        path = './urls.txt'
        with open(path, 'a') as f:
            f.writelines(url)
            f.writelines('\n')

if __name__ == '__main__':
    ON=1
    i = 98
    while ON:
        try:
            i+=+1

            z =ZanMei()
            # if z.isurl(str(i)) == True:
                # print(z.isurl(str(i)))
            z.wisurl(str(i))

            html = z.parse_html(i)
            title =html[0]
            url = html[1]
            time.sleep(3)
            img = z.contentsAndtitle(url)
            z.download(title,img)
            # else:
            #     print('已下载')
        except:
            ON = 0
            print('程序错误')