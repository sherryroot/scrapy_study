import  requests
import json

api_url="https://proxy.horocn.com/api/proxies?order_id=GTCS1629257787943740&num=3&format=text&line_separator=win&can_repeat=yes"

r=requests.get(api_url)
#r=['27.150.117.94:35480\r', '60.168.244.143:50281\r', '183.149.77.88:53285']

#print(r.text)

for ip_text in r:
    ip_str=str(ip_text,encoding="utf-8")
    #ip=ip_text.split('\n')
    ip = ip_str.split('\n')
    for i in ip:

        a=i.strip('\r')

        print(a)
