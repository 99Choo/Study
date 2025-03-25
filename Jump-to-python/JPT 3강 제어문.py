# 조건문, 반복문
# money = True
# if (money): 불 자료형 <,>,==,!=,>=,<=,and,or,not,in,not in
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# if 조건문:
#   수행할 문장 1
#   수행할 문장 2

# else:
#   수행할 문장 A
#   수행할 문장 B

# 다중 조건 판단 elif
# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     print("택시를 타고가라")
# elif card:
#     print("택시를 타고가라")
# else:
#     print("걸어가라")

# while문의 기본 구조
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
# ...

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다. " % treeHit)
#     if treeHit == 10:
#        print("나무 넘어갑니다.")

# break
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break
 
# continue 
# a = 0
# while a < 10:
#     a = a+1
#     if a % 2 == 0: continue
#     print(a)

# 무한 루프
# while True:
    # 수행할 문장1
    # 수행할 문장2

# for문 기본구조
# for 변수 in 리스트(또는 튜플, 문자열):
    #   수행할 문장1
    #   수행할 문장2

# for와 함께 자주 사용하는 range함수
# sum = 0
# for i in range(1, 11):
    # sum = sum + i

# print(sum)

# 구구단
# for i in range(2,10):
    # for j in range(1, 10):
            # print(i*j, end=" ")
    # print('')