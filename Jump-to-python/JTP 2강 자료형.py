# 숫자, 문자열, 불 변수, 리스트, 튜플, 딕셔너리, 집합

# print(type()) 출력되는 값의 정의 알기

# 변수 = a = a + 1 a = 3 a라는 변수 안에 3을 넣는다.

# 정수형 (1, 2, -2) int 

# 실수 (1.24, -34.56) float

# 컴퓨터식 지수 표현 방식 (4.24e10, 4.24e-10)

# 제곱  a = 3
        # b = 4
        # a ** b = 81

# 나머지 구하는 법
# a = 3
# b = 4
 
# print(a%b)

#  연산자 7/4 7//4 = 몫
# 1.75 / 1

# 문자열 자료형 만드는 4가지 방법
# a = "Hello World"
# a ='Python is fun'
# a = """Life is too short,
# You need python"""
# a = '''Life is too short, You need python'''

# """ 를 사용하면 /n을 쓰지않고도 띄워쓰기와 다음줄 변환"""
# print(a)

# 문자열에 따옴표 포함시키기

# food = "Python's favorite food is perl"
# say = '"Python' is very easy. " he says.'
# food = 'Python\'s favorite food is perl"
# say = "\"Python is very easy.\" he says."

# 여러 줄로 이루어진 문자열
# a = "Life is too short\nYou need python"
# print(a)

# 문자열 더해서 연결하기 

# head = "Python"

# tail = " is fun! "

# a = head + tail

# 'Python is fun!'

# print(a)

# 문자열 곱하기
# a = 'python'

# b = a * 2

# print (b)

# 인덱싱
# a = "Life is too short, You need Python"

# a[0] 'L'

# a[12] 's'

# a[-1] 'n'
 
# 슬라이싱
# a = "Life is too short, You need Python"
# a[0:4] "Life"

# a = "20010331Rainy"
# date = a[:8]
# '20010331'  a[ : : ] 이상 미만 간격

# print(a[])

# 문자열 포매팅

# "I eat %d apples." % 3 = 'I eat 3 apples.'

# number = 10 / day = "three"

# "I ate %d apples. so I was sick for %s days." % (number, day)
# 'I ate 10 apples. so I was sick for three days.'

# 정렬과 공백
# "%10s" % "hi"
# '     hi'
# "%-10sjane. " % 'hi'
# 'hi   jane.'

# 문자열 개수 세기(count)

#  a = "hobby"
# a. count('b') = 2

# 위치 알려주기1(find)

#  a = "Python is best choice"

#  a. find('b')
#  10

#  a.find('k") 없으면 -1 출력됨.
#  -1

#  위치 알려주기2(index)
#  a = "Life is too short"
#  a.index('t')
#  8

# a. index('k')  
#  Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  ValueError: substring not found

# 문자열 삽입('join')
# a = ","
# a. join('abcd')
# 'a,b,c,d'

# 소문자를 대문자로 바꾸기(upper)
# a = "hi"
# a. upper()
# 'Hi'

# 대문자를 소문자로(lower) 
# a = "h1"
# a.lower()
# 'hi'

# 문자열 바꾸기(replace) 
# a = "Life is too short"
# a.reaplace("Life", "Your leg")
# 'Your leg e is too short' 

# 문자열 나누기 (split)
# a = "Life is too short"
# a.split()
# ['Life', 'is', 'too', 'short']
# a = "a:b:c:d"
# a.split(':')
# ['a', 'b', 'c', 'd']

# 리스트는 변수를 한 번에 관리한다. 
# 
# odd = [1, 3, 5, 7, 9]
# 
# 리스트명 = [요소1, 요소2, 요소3, ...]
# a = [ ]
# b = [1, 2, 3]
# c = ['Life', 'is', 'too', 'short'] 
# d = [1, 2, 'Life', 'is']
# e = [1, 2, ['Life', 'is']]

# 리스트의 인덱싱
# a = [1, 2, 3]
# a[0]
# 1

#a[0] + a[2] 
# 4

# a[-1]
# 3

# 리스트 더하기
# a = [1, 2, 3]
# b = [4, 5, 6]
# a + b
# [1, 2, 3, 4, 5, 6]

# 리스트 반복하기
# a = [1, 2, 3]
# a * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트에서 하나의 값 수정하기
# a = [1, 2, 3]
# a[2] = 4
# a
# [1, 2, 4]

# 리스트에서 연속된 범위의 값 수정하기
# a[1:2]
#[2]
#a 
# a[1:2] = ['a', 'b', 'c']

# [] 사용해 리시트 요소 삭제하기 
# a = [1, 'a', 'b', 'c', 4]
# a[1:3] = []
# a
# [1, 'c', 4]
 
# del 함수 사용해 리스트 요소 삭제하기
# a
# [1, 'c', 4]
# del a[1]
# a
# [1, 4]

# 리스트에 요소 추가(append) 
# a = [1, 2, 3]
# a.apped[4]
# [1, 2, 3, 4]

# 리스트 정렬(sort) 
# a = [1, 4, 3, 2]
# a.sort()
# a [1, 2, 3, 4] 

# 리스트 뒤집기(reverse)
#  a = ['a', 'c', 'b']
#  a.reverse()
#  a
#  ['b', 'c', 'a']

# 위치 반환(index)
#  a = [1,2,3]
#  a.index(3)
#  2

# 리스트에 요소 삽입(insert)
# a = [1, 2, 3]
# a.insert(0, 4)
# [4, 1, 2, 3]

#  리스트 요소 제거(remove)
#  a = [1, 2, 3, 1, 2, 3]
#  a.remove(3)
# [1, 2, 1, 2, 3]

# 리스트 요소 끄집어내기(pop)
# a = [1, 2, 3]
# a.pop()
# 3
# a
# [1, 2]

# 리스트에 포함된 요소 x의 개수 세기(count)
# a = [1,2,3,1]
# a.count(1)
# 2

# 리스트 확장(extend)
# a = [1,2,3]
# a.extend([4,5])
# a
# [1, 2, 3, 4, 5]
# b = [6, 7]
# a.extend(b)
# a
# [1, 2, 3, 4, 5, 6, 7]

# 정수형 (1, 2, -2) int

# 실수 (1.24, -34.56) float

# 제곱
# a = 3 
# b = 4
# a ** b
# 81

# % 연산자
# 7 % 3
# 1

# 3 % 7 
# 3

# 7 