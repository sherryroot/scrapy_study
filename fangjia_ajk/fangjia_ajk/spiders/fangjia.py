import scrapy
import csv
from fake_useragent import UserAgent
import  random
import re
from scrapy.scrapy_BOT_ANJVKE.spiders.fangjia_ajk.fangjia_ajk.items import FangjiaAjkItem

import numpy as np
import pandas as pd


class FJ_spider(scrapy.Spider):

    name='FJ'
    def read_wbs(self):
        temp=[]
        df = pd.read_csv(
            "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/scrapy/scrapy_BOT_ANJVKE/spiders/ajk/ajk/r.csv")
        urls = df['wbs']

        for i in urls:
            temp.append(i)
        return temp


    def Radom_header(self):
        ua = UserAgent();
        i = random.randint(1, 5)
        print("heard is from Browser")
        print(i)
        if i == 1:
            Browser = ua.ie
        elif i == 2:
            Browser = ua.firefox
        elif i == 3:
            Browser = ua.chrome
        elif i == 4:
            Browser = ua.safari
        else:
            Browser = ua.random
        return Browser

    def start_requests(self):


        #for page_addr in temp_addr:
            h = FJ_spider.Radom_header(self)
            header = {"User-Agent": h}
            print("I AM CRAWLING ______________")
            #urls=["http://www.anjuke.com/fangjia/shanghai2019/","http://www.anjuke.com/fangjia/shanghai2018/"]
            urls=FJ_spider.read_wbs(self)
            print(urls)
            for start_url in urls:
                print("here I am")
                start_url=start_url.strip()
                start_url=start_url.strip('"')
                print(start_url)
                try:
                    yield scrapy.Request(url=start_url, headers=header)

                except:
                    print("//something is wrong in crawling\\ ")
                #print(page_addr)
                    pass

    def parse(self, response):
        content = response.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul').extract()
        #print(content)
        for year_price in content:
            pattern_0 = re.compile('2\d\d\d年\d?.')
            time = pattern_0.findall(year_price)
            print(time)
            pattern_1=re.compile('\d{5}元/㎡')
            price=pattern_1.findall(year_price)
            print("price is")
            print(price)
            ##
            item = FangjiaAjkItem()
            i=0

            while i>=0:
                    try:

                        item['time']=time[i]
                        item['price']=price[i]
                        i=i+1
                        yield item
                    except:
                        i=-1







