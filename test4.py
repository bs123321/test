# a = 0
#
# while a < 5:
#     print("Мы в цикле")
#     a = a + 1
#     if a == 3:
#         a = a + 1
# else:
#     print("Закончили выполнение цикла while")
#     b = 100
#     while b >= 0:
#         print(b)
#         b = b - 1

for i in range(1, 100):
    if i % 3 == 0:
        print(i)
