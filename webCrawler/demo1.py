# !/usr/bin/python3

# 抓取简书网站首页文章的标题和文章链接

# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
from urllib import request
# Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库
from bs4 import BeautifulSoup

# 构造头文件，模拟浏览器访问
url = "http://www.jianshu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request .Request(url, headers=headers)
page_info = request.urlopen(page).read().decode(
    'utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody


# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')

# 以格式化的形式打印html
# print(page_info)

titles = soup.find_all('a', 'title')  # 查找所有a标签中class='title'语句

# open()是读写文件的函数，with语句会自动close()已打开文件

# 在磁盘以只写的方式打开/创建一个名为 demo 的txt文件

with open(r"F:\gylwork\test\ggg.txt", "w") as file:
    for title in titles:
        file.write(title.string+'\n')
        file.write("http://www.jianshu.com" + title.get('href')+'\n\n')
