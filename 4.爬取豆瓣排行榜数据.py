from email import header
import requests
import re


a = 0
b = 0

while(a<100):
    # 获取网站HTML内容
    url = f"https://movie.douban.com/top250?start={a}&filter="
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
    }
    resp = requests.get(url, headers=header)
    content = resp.text

    # 解析数据
    obj = re.compile(r'<span class="title">(?P<name>.*?)</span>.*?</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<mark>.*?)</span>.*?<span>(?P<comment>.*?)</span>', re.S)

    # 匹配输出
    res = obj.finditer(content)
    for i in res:
        print("序号：" ,b)
        print("电影名字:", i.group("name"))
        print("年份:", i.group("year").strip())  # strip()用来消除年份前面的空白区域
        print("评分:", i.group("mark"))
        print("评论量:", i.group("comment"))
        b +=1
        print("--------------------------------------------------------------------------")
    
    
    a += 25
    

# 结束进程
print("--------------------------------------------------------------------------")
resp.close()
print(b)
print("end!")
