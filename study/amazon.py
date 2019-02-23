#encoding=utf-8
import requests
url="https://www.amazon.cn/b/ref=cgit_zdp_ags_1499867071_t?_encoding=UTF8&ie=UTF8&node=1499867071&pf_rd_p=51192ffa-b357-465e-87a5-94e008193575&pf_rd_s=desktop-1&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=FBPZMKDZB9BKRBZAJ7AN&pf_rd_r=FBPZMKDZB9BKRBZAJ7AN&pf_rd_p=51192ffa-b357-465e-87a5-94e008193575"
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print r.text[1000:2000]
except:
    print "爬取失败"