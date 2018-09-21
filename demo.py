# n = 123
# f = 456.789
# s1 = 'hello,world'
# s2 = 'hello,\'lily\''
# s3 = r'hello,"Bart"'
# s4 = r'''hello,
# lisa!'''

# print(s1)
# print(s2)
# print(s3)
# print(s4)


# wet = int(input("小明的体重为："))

# if wet < 18.5:
#     print('过轻')
# elif wet >= 18.5 and wet < 25:
#     print('正常')
# elif wet >= 25 and wet < 28:
#     print('过重')
# elif wet >= 28 and wet < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# n1 = 255

# a = hex(n1)
# print(a)


import math


# def quadratic(a, b, c):
#     if not(isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
#         raise TypeError('a，b，c只能为数字')
#     if a == 0:
#         return '请输入不等于0的a值'
#     else:
#         d = math.pow(b, 2) - 4*a*c
#         if d < 0:
#             return '无实根'
#         elif d == 0:
#             res = -b/(2*a)
#             return res
#         else:
#             res1 = (-b + math.sqrt(d))/(2*a)
#             res2 = (-b - math.sqrt(d))/(2*a)
#             return res1, res2


# print(quadratic(1, 2, 1))
# print(quadratic(1, 1, 1))
# print(quadratic(1, 3, 1))

# def enroll(name, gender, age=6, city='CHAGNSHA'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)


# enroll('Adam', 'M', 7, 'Tianjin')

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())
