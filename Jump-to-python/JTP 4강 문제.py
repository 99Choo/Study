# def is_odd(number):
#     if number%2==1:
#         return True
#     else:
#         return False
# print(is_odd(1))

# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i 
#     return result/len(args)

# print(avg_numbers(1, 2))
# print(avg_numbers(1,2,3,4,5))

# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번째 숫자를 입력하세요:"))

# total = input1 + input2
# print("두 수의 합은 %d 입니다" % total)

# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you","need","python")
# print("!!".join(["you","need","python"])) x

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("test.txt", 'r')
# print(f2.read())

# user_input = input("저장할 내용을 입력하세요:")
# f = open('test.txt','a')
# f.write(user_input)
# f.write("\n")
# f.close()

# f = open('text.txt', 'r')
# body = f.read()
# f.close()

# body = body.replace("java","python")

# f = open('test.txt','w')
# f.write(body)
# f.close()