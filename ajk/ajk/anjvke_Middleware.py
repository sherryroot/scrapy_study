import time,random,logging
#add random delay time
class RandomDelayMiddleware(object):
    def __init__(self):
        self.delay=3
    def process_request(self,request,spider):
        delay=random.randint(0,self.delay)
        logging.debug("###random delay:%s s###"%delay)
        print("#########sherry_test_dealy###########")
        time.sleep(delay)

##set Proxy

class ProxyMiddleware(object):
    def __init__(self):
        #r = ['218.95.97.189:328620', '61.174.157.94:33423', '125.117.213.225:31975']
        r=['123.55.1.145:49736','123.180.209.72:47086']

        self.ip=r

    def process_request(self,request,spider):
        try:
            ip=random.choice(self.ip)
            request.meta['proxy']=ip
            print("_____proxy has been changed_____")
        except:
            pass





