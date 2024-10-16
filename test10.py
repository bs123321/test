# №1
from itertools import count

# string = input()
#
# if 0 < int(string[0]) > 100:
#     print("Введенное число вне диапазона")
# else:
#     number = int(string)
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     if number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     if number % 15 == 0:
#         print("Fizz Buzz")
#     else:
#         print(number)
#
# №2
#
# string = input("Введите число и степень: ").split(" ")
# number = int(string[0])
# stepen = int(string[1])
#
# if stepen >= 0 and stepen <= 7:
#     result = number ** stepen
#     print(result)

# №3

# string = input("Введите стоимость, с кого звоним, куда звоним: ").split(" ")
#
# price = float(string[0])
# mtot = 0 # 0.2
# mtob = 1 # 0.3
# ttob = 2 # 0.4
# mtom = 3 # 0.1
# btob = 4 # 0.1
# ttot = 5 # 0.1
#
# if string[1] == "m" and string[2] == "t":
#     result = price * 0.2
#     print(result)
# elif string[1] == "m" and string[2] == "b":
#     result = price * 0.3
#     print(result)
# elif string[1] == "t" and string[2] == "b":
#     result = price * 0.4
#     print(result)
# elif string[1] == "m" and string[2] == "m":
#     result = price * 0.1
#     print(result)
# elif string[1] == "b" and string[2] == "b":
#     result = price * 0.1
#     print(result)
# elif string[1] == "t" and string[2] == "t":
#     result = price * 0.1
#     print(result)

# №4
#
# string = input().split(" ")
#
# number = []
# volume_all = []
# for i in string:
#     volume_all.append(int(i))
# premia = 200
# max_volume = 0
#
# for i in string:
#     volume = int(i)
#     zp = 200
#     max_volume = max(premia, volume)
#     if 0 < volume < 500:
#         zp *= 1.03
#     elif 500 <= volume <= 1000:
#         zp *= 1.05
#     elif volume > 1000:
#         zp *= 1.08
#     # print(zp)
#     number.append(zp)
#     # print(number)
#
# count_max = 0
# for i in string:
#     max_volume = max(volume_all)
#     if max_volume == int(i):
#         count_max += 1
#
# print(count_max)
#
# k = 0
# for i in string:
#     max_volume = max(volume_all)
#     print(max_volume)
#     if max_volume == int(i):
#         print("макс объём", i)
#         number[k] += premia / count_max
#     k += 1
# print(number)

