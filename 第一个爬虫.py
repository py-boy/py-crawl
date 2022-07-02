from urllib.request import urlopen

url = "https://www.runoob.com/python/python-files-io.html"
resp = urlopen(url)

# print(resp.read().decode("utf-8"))


# 下面会报错的原因为：Python3给open函数添加了名为encoding的新参数，而这个新参数的默认值却是‘utf-8’。这样在文件句柄上进行read和write操作时，系统就要求开发者必须传入包含Unicode字符的实例，而不接受包含二进制数据的bytes实例。

# 解决方法：
# 使用二进制模式（"wb"、"rb"）来开启待操作文件

# python file 方法：https://www.runoob.com/python/file-methods.html

# with open("爬取的第一个网页.html", mode="w") as f:
#     f.write(resp.read())
# print("完成！！！")



with open("爬取的第一个网页.html", mode="wb") as f:
    f.write(resp.read())
print("完成！！！")