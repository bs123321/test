# import re
#
# s = input("Введите логин: ")
#
# pattern = "(user)|(admin)+"
# st = re.search(pattern, s)
# print(st)
# if not st:
#     print("Логин верный", s)


# TESTDOP

# найти наибольшее число в массиве, являющееся полным квадратом некоторого числа
#
# s = input().split(" ")
# num = []
# maxSquare = 0
# for i in range(int(s[0]), int(s[1])):
#     sqrt = int(i ** 0.5)
#     # print(sqrt*sqrt)
#     if i == sqrt * sqrt:
#         num.append(i)
# print(num)