#!/usr/bin/python3

# 打开文件

fo = open('test.txt', 'wb')
print('文件名为：', fo.name)

# 关闭文件
fo.close()
