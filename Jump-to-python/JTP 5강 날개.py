#  immutable (정수,실수,문자열,튜플)
#  튜플:변하지 않는다.
# a = 1
# def vartest(a) :
#    a = a + 1

# vartest(a)
# print(a)

# Mutable (리스트,딕셔너리,집합)
# 값이 변함
# b =  [1,2,3]
# def vartest2(b):
#    b = b.append(4)

# vartest2(b)
# print(b)


# result = 0
# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(4))

# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# Calculator 맨 첫글자 대문자로 __init__ 어떤 값을 설정할지, 설정해 주는 부분
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num 
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# pass=내부 동작은 필요 없고, 의미적으로 껍데기만 필요한 경우
# class FourCal:
#     pass

# a = FourCal()
# print(a)
# # 어떤 객체인데 FourCal이라는 클래스로 만든 객체다.

# class FourCal:
#     pass

# a = FourCal()
# print(type(a))
# 클래스로 만든 기본설계도를 만들고 이 설계도로 찍어서 변수에 넣는다.
# 클래스 안에 있는 함수=메서드

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
    
# a = FourCal()
# a.setdata(1,2)
# print(a.first)
# print(a.second)

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add (self):
#         result = self. first + self.second
#         return result
    
# a  = FourCal()
# a. setdata(4,2)
# print(a.add())



# __init__ 예약어,맨앞에 쓸 것
# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata (self, first, second):
#         self.frist = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
    
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result


# 공통으로 쓸때는 클래스 변수. 각각 개체마다는 객체 변수.

# class FourCal:
#     first = 2 
#     second = 3
#     # def __init__(self, first, second):
#     #   self.first = first
#     #   self.second = second
#     def setadat(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
# a = FourCal()
# print(a.first)
# b = FourCal()
# print(b.first)

# class Family:
#     lastname = "김"
# Family. lastname = "박"
# print(Family.lastname)

# a = Family() 
# b = Family()
# print(a. lastname)
# print(b. lastname)

# 모듈?=미리 만들어 놓은 .py 파일 (함수,변수,클래스)
# import (파일이름) form (파일이름) import (함수)

# from mod1 import add

# print(add(1,2))

# import mod1

# import sys
# sys.path.append("C:\\jpt.py\\subFolder")
# import mod1
# print(mod1.add(3,4))

#  패키지=라이브러리,모듈 여러 개 모아놓은 것
# from (폴더).(파일).() import (파일이름) as (이름줄여서)
# from (폴더).(파일).() import * = 싹다 불러오기

# from (폴더).(파일).() import (파일)
# ../../ 이전 폴더로 돌아간다.
# def ㅁ_test():
#     print("render")
#     a() ㅁ테스트라는 함수를 렌더라는 파일에 쓸 때.

# 예외 처리=오류가 발생했을때 어떻게 할지 정하는 것 
# try: #오류가 발생할 수 있는 구문

# except Exception as e: #오류가 발생

# else : #오류 발생하지 않음

# finally: #무조건 마지막에 실행

# 오류가 발생할 수 있는 구문, 오류 발생시 e에 구문저장하고 출력
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# try를 해서 성공 했을 때, 구문에 오류가 없을 때 else를 실행
# try:
#      f = open('none', 'r')
# except FileNotFoundError as e:
#      print(str(e))
# else:
#      data = f.read()
#      print(data)
#     #  f.close() 

# try:오류 날 수 있는걸 시도 except:오류 났을때 잡는 거 finally:오류 나도 마지막에 실행.
# f = open('foo.txt' 'w')
# try:
#     # 무언가를 수행한다.
#     # Exception: 어떤 에러든 다 잡을 수 있다.
#     data = f.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# except로 해서 여러 개의 예외 처리 조건을 걸어서 각각에 맞춰 다르게 처리o
# try:
#     a =  [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱할 수 없습니다.")

# except로 오류를 잡고 pass를 넣으면 그냥 지나가라고 설정o
# try:
#     f = open("나없는파일", 'r')
# except FileExistsError:
#     # pass

# 일부러 오류를 낼 때 raise 뒤에 오류 이름을 적으면 실행했을 때 오류가 발생
# class Bird:
#     def fly(self):
#         raise NotImplementedError
    
# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagel = Eagle()
# eagel.fly()

# 내장함수 =파이썬에서 기본적으로 포함하고 있는 함수 ex)print(),type() abs=절댓값

# all([1, 2, 3])= 모두 참인지 검사

# any([1, 2, 3, 0]) any([0, ""])= 하나라도 참이 있는가?

# chr()=아스키 코드를 입력받아 문자 출력

# dir=자체적으로 가지고 있는 변수나 함수를 보여줌

# divmod(7, 3) (2, 1)= 몫과 나머지를 튜플 형태로 돌려줌

# enumerate=열거하다. for i,name in enumerate(['body', 'foo', 'bar']) print(i, name)

# eval=실행 후 결과값을 돌려줌 eval('1+2') 3

# filter=합수를 통과하여 참인 것만 돌려줌
# def positive(x):
    # return x > 0

# a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
# print(a)

# id=주소 값 a=3 id(3) 

# input= 사용자 입력 받는 함수 a =input()

# int(10진수 정수 형태로 변환) int('3')

# len=길이 len("python") 6

# map 각 요소가 수행한 결과를 돌려줌
# def two_times(x): return x*2
# a = list(map(two_times, [1, 2, 3, 4]))
# print(a)

# max=최대 값 max([1, 2, 3]) 3 min=최소 값 min([1, 2, 3]) 1

# open = 파일 열기 f = open("binary_file", "rb")

# pow = 제곱한 결과값 반환 pow(2, 4) 16 2의 4승

# range=범위 list(range(5)) [0, 1, 2, 3, 4]

# round=반올림 round(4.6) 5

# sorted=정렬 sorted([3, 1, 2]) [1, 2, 3]

# str=문자열 반환 str(3) 3 str('hi') 'hi'

# tuple=튜플 반환 tuple("abc") ('a', 'b', 'c')

# type=타입을 출력 type("abc") <class 'str'

# zip=자료형을 묶어주는 역할 list(zip([1, 2, 3], [4, 5, 6])) [(1, 4), (2, 5) (3, 6)]

# 외장함수=라이브러리 함수, import 해서 쓰는 것

# pickle=외장함수 
# import pickle
# f = open("test.txt", 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()

# time-외장함수
# import time
# print(time.time())
#1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간 초 

