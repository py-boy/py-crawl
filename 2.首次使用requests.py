import requests

# a = input("请输入你要查找的关键字")
url = f"https://www.baidu.com/"#在字符串前添加“f”，即可在字符串中添加变量

#添加请求头，是一种反爬手段
b = {

    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
                             
}

resp = requests.get(url,headers=b)

# print(resp.text)

with open("首次使用requests框架.html", mode="wb") as c:
    c.write(resp.content)

print("完成！！！")
