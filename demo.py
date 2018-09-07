#!/usr/bin/python3

# 用户输入数字
# num1 = input("输入第一个数：")
# num2 = input("输入第二个数：")

# sum = float(num1)+float(num2)

# print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


# 平方根

# import math

# num = float(input('请输入一个数字：'))
# num_sqrt = math.sqrt(num)

# print(num_sqrt)

# 二次方程

# import cmath

# a = float(input('输入a:'))
# b = float(input('输入b:'))
# c = float(input('输入c:'))

# d = (b**2) - (4*a*c)

# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b-cmath.sqrt(d))/(2*a)

# print('结果为{0}和{1}'.format(sol1, sol2))


# 计算三角形面积

# a = float(input('输入三角形第一边长：'))
# b = float(input('输入三角形第二边长：'))
# c = float(input('输入三角形第三边长：'))

# L = (a+b+c)/2

# S = (L*(L-a)*(L-b)*(L-c))**0.5

# print('三角形面积为%0.2f' % S)


# python随机数

# import random

# print(random.randint(0, 9))


# 摄氏度转华氏温度

# celsius = float(input('输入摄氏温度为：'))

# fahrenheit = (celsius*1.8) + 32

# print('%0.1f 摄氏温度转为华氏温度为 %0.1f' % (celsius, fahrenheit))


# 判断是否为质数
# 质数是大于1的自然数，并且只能被1和自身整除

num = int(input('请输入一个数字：'))

if num > 0:
    for i in range(2, num):
        if(num % i == 0):
            print(num, '不是质数')
            break
    else:
        print(num, '是质数')
else:
    print(num, '不是质数')
