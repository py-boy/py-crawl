from email import header
import requests

url = "https://movie.douban.com/typerank?"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}

# url后面所带的参数,以字典的显示展现,可在F12中的负载查得
param = {
    "type": "11",
    "interval_id": "100:90",
    "action":"" ,
    "start": "0",
    "limit": "20"
}

resp = requests.post(url=url,params=param,headers=header)

# print(resp.text)
with open("爬取豆瓣排行榜.html", "wb") as f:
    f.write(resp.content)
print("over!!!")

# 一定要加一个关闭爬虫的指令
resp.close()
print("close")