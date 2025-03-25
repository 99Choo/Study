# 1.
# 함수작성시 결과값이 안나올수도 있다.
# def sum(a,b):
#     result = a + b
#     return result
# print(sum(1,2))

# 입력값이 없어도 그냥 출력값만 있을 수 있다.
# def say():
#     return 'Hi'

# print(say())

# 2.
# 출력값이 없을수도 있다. return result가 없음. 함수내에서 자체적 처리
# def sum(a,b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# print(sum(1,2))

# 이 함수는 입력도 출력도 없다. ruturn이 없음. 
# def say():
#     print('Hi')
# print(say())

# 3.
# 여러개 넣을 때 표현 (*args) *args말고 다르게 표현가능. in앞에 똑같이 고쳐줄것.
# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(sum_many(1,2,3,4,5,6))

# 4.
# keyword argument : dictionary 형태로 여러 개의 값이 들어올 수 있는 처리가능한 매개변수.
# def print_kwargs(**kwargs):
#     for k in kwargs.keys():
#         if(k == "name"):
#             print("당신의 이름은 :" + k)
# print(print_kwargs(name="int 조수", b="2"))

# sum_and_mul = a,b더한 값,곱한 값을 한 번에 return, 튜플 형태로 나옴, 하나씩 나눠쓰면됨 따로 뽑아 쓸수도 잇음
# def sum_and_mul(a,b):
#     return a+b, a*b

# print(sum_and_mul(1,2)[0])

# 5.
# 함수는 맞춰서 적을것 True를 적으면 항상 출력됨 기본값으로 설정한 것은 맨뒤에 적을것
# def say_myself(name, old, man=True):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
# say_myself("라이유튜브",20,)       

# 6.
# (a) 임시변수,지역변수 a라는 값이 밖에 영향을 주지 못함. a = a +1 별도의 독립된 변수이다.
# global = 바깥 전체에 사용할 수 있는 변수
# a = 1
# def vartest():
#     global a
#     a = a +1

# vartest()
# print(a)

# 7.
# lambda
# def add(a,b):
#     return a+b

# def와 동일한 역할
# myList = [lambda a, b : a+b, lambda a, b: a*b]

# print(myList[1](1,2))

# input=(내장함수) print문 ""로 둘러싸인 문자열은 + 연산과 동일하다
# 문자열 띄어쓰기는 콤마로 한다.
# print("Life" "is" "too short")
# print("life","is","too short")

# end=' ' 이 띄어쓰기를 그냥 i 뒤에 붙여서 계속 출력을 하겠다.
# for i in range(10):
    # print(i, end="hi")

# 8.
# f = open("파일 이름", 파일 열기 모드)
# r = 읽기 모드 -파일을 읽기만 할 때 사용
# w = 쓰기 모드 -파일에 내용을 쓸 때 사용
# a = 추가 모드 -파일의 마지막에 새로운 내용을 추가할 때 사용
# f = open("새파일".txt", 'a')
# f.close()

# 9.
# 절대주소 : 처음부분(C:/)부터 주소를 쓰는 것. 상대주소 : 현재 실행하는 파일을 기준으로 상대적인 경로를 써주는 것
# \n = 한줄 띄워주기 encoding 사용자가 입력한 문자나 기호들을
# f = open("C:/doit/새파일.txt", 'w' encodint="UTF-8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# READLINE=어떤 파일이 있으면 그중에 한줄씩 읽어오는 함수
# f = open("C:/doit/새파일.txt", 'r' encoding="UTF-8" )
# line = f.readline():
# print(line)
# f.close()

# readline=한줄 읽어오기 
# f = open("새파일.txt", 'r' )
# while True:
#     line = f.readline():
#     if not line: break
#     print(line)
# f.close()

# readlines=리스트 형태로 가져와서 출력
#  strip("\n", end=" ")
#  f = open("새파일.txt", 'r' )
#  lines = f.readlines()
#  for line in lines:
#     print(line)
#  f.close()

# # read=통째로 다 불러올때
# f = open("C:/doit/새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# with문과 함께 사용하기
# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")

# a는 전체 수정 w는 뒤에 줄 추가

# 