# №1

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

string = input().split(" ")

# manager1 = int(string[0])
# manager2 = int(string[1])
# manager3 = int(string[2])
#
# for i in string:
# #     zp_all.append(int(i))
# # zp_all.sort(reverse=True)
# # print(zp_all[0])

base = 200
percent = 0
premiya = 0

status = 0
if (int(string[0]) > int(string[1]) > int(string[2])
        or int(string[0]) > int(string[2]) > int(string[1])):
    status = 0
if (int(string[1]) > int(string[2]) > int(string[0])
        or int(string[1]) > int(string[0]) > int(string[2])):
    status = 1
if (int(string[2]) > int(string[1]) > int(string[0])
        or int(string[2]) > int(string[0]) > int(string[1])):
    status = 2

k = 0
for i in string:
    zp = int(i)
    if 0 < zp < 500:
        percent = 0.03
    elif zp <= zp < 1000:
        percent = 0.05
    elif zp >= 1000:
        percent = 0.08

    if k == status:
        premiya += 200
        print("Менеджер №:" ,k+1, ", ", base * (1 + percent) + premiya)
    else:
        print("Менеджер №:" ,k+1, ", ", base * (1 + percent))
    k += 1

