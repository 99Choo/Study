# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val
# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#       self.value -= val  
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)


# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val
# class maxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:      
#             self.value = 100
# cal = maxLimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)

# 내장함수 안에서 0은 거짓이다.
# p232
# print(all([1, 2, abs(-3)-3]))
# p233
# print(chr(ord('a')) == 'a')


# print(list(filter(lambda x : x > 0,  [1, -2, 3, -5, 8, -3])))

# print(hex(234))
# print(int(0xea))

# print(list(map(lambda x : x*3 , [1, 2, 3, 4])))

# a = [-8, 2, 7, 5, -3, 5, 0, 1]
# print(max(a)+min(a))

# print(round(17 / 3, 4))

# import time

# print(time.strftime('%Y/%m/%d %H:%M:%S'))

# import random
# lotto = sorted(random.sample(range(1,46), 6))
# print(lotto)