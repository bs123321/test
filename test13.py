# # while True:
# #     chislo = int(input())
# #
# #     if chislo == 7:
# #         print("Goodbye")
# #         break
# #     elif chislo > 0:
# #         print("Положительное")
# #     elif chislo < 0:
# #         print("Отрицательное")
# #     elif chislo == 0:
# #         print("Ноль")
# import time
# from datetime import datetime
#
# string = input().split(" ")
# numbers = []
# start_time = datetime.today()
# for i in range(int(string[0]), int(string[1])):
#     # print(i)
#     count = 0
#     j = 1
#     while j <= i:
#         # print(j)
#         if i % j == 0:
#             count += 1
#         if count > 2:
#             break
#         j += 1
#     if count == 2:
#         numbers.append(i)
# end_time = datetime.today()
#
# delta = end_time - start_time
# print(delta)
# print("Простые числа", numbers)
