import scrapy
from fake_useragent import UserAgent
import  random
import re

##change headers

class TEST_Item(scrapy.Item):
    # define the fields for your item here like:
    year= scrapy.Field()
    price=scrapy.Field()
    wbs=scrapy.Field()
    print("^^^^^^^^^^I have_123_ run ITems^^^^^^^^^")




class TEST(scrapy.Spider):
    name="ajk"
            ##return data
    def scrapy_price(self,wb_addr):
        h = TEST.Radom_header(self)
        header = {"User-Agent": h}
        yield scrapy.Request(url=wb_addr, headers=header)
        TEST.anjvke_az(self,response)



    def anjvke_az(self,response):
        content=response.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul').extract()
        print(content)
        for month in content:
            pattern=re.compile()
           # M_Time = pattern.findall('//html/body/div[2]/div[5]/div[1]/div[1]/ul/li[2]/a/b').extract()
           # Price=response.xpath('//html/body/div[2]/div[5]/div[1]/div[1]/ul/li[2]/a/b').extract()




    def Radom_header(self):
        ua = UserAgent();
        i=random.randint(1,5)
        print("heard is from Browser")
        print(i)
        if i==1:
            Browser=ua.ie
        elif i==2:
            Browser=ua.firefox
        elif i==3:
            Browser=ua.chrome
        elif i==4:
            Browser=ua.safari
        else:
            Browser=ua.random
        return Browser



    def start_requests(self):
        #start_urls = 'http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html'
        start_urls = 'https://www.anjuke.com/fangjia/shanghai/'
        h=TEST.Radom_header(self)
        header={"User-Agent":h}
        yield scrapy.Request(url=start_urls,headers=header)

    def website_clean(self,data):

        for str in data:
            print("str is")
            print(str)
            wbsite=str.replace("href=","")
            print("wbsite is")
            print(wbsite)
            print("%%%%%123%%%%%%")
            print(wbsite)
            TEST_Item.item['wbs']=wbsite
            yield TEST_Item.item


    def parse(self,response):

       the_agent=response.request.headers['User-Agent']
       ip_meta=response.request.meta
       print("______________________________")
       print(the_agent)
       print("*************aa****************")
       content=response.xpath('/html/body/div[2]/div[3]/div[1]').extract()

       for year_text in content:
           pattern=re.compile('href="h.*/"')
           ws = pattern.findall(year_text)
           #print("############here is ws")
           #print(ws)
           #TEST.website_clean(self,ws)

           for str in ws:
               item=TEST_Item()
               wbsite = str.replace("href=", "")
               print("wbsite is")
               print(wbsite)
               item['wbs'] = wbsite
               yield item











       print("************end*****************")




