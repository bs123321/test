# import  re
#
# string = input("Введите число ")
#
# if float(string) > 0:
#     print("положительное")
# elif float(string) < 0:
#     print("отрицательное")
# else:
#     print("число равно 0")
#
#

# print(re.sub(r'[^.\d]',"", string))
# number = [0, 0]
# numbers = re.findall(r'[-+^.]?\d+', string)
# try:
#     number[0] = float(numbers[0])
# except:
#     number[0] = 0
# try:
#     number[1] = float(numbers[1])
# except:
#     number[1] = 0
#
# ishodnoe = number[0] + number[1]
