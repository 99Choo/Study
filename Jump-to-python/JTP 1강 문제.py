# Q1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동  씨의 평균 점수를 구해보자.
# 국어 80 영어 70 수학 55
# a = 80
# b = 70
# c = 55

# d = round(((a+b+c)/3),1)

# print(d)

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에  대해 말해보자.
# 1 % 2 = 1
# 2 % 2 = 0
# print(13 % 2)  

# 2로 나눴을때 0이 나오면 짝수 1이 나오면 짝수 . 따라서 13은 홀수.

# Q3.  주민등록번호를 연월과 그 뒤의 숫자 부분으로 나누어  출력해 보자.
# pin = "881120-1068234"
# yyyymmdd 
# num
# print(pin[0:6])
# print(pin[7:])

# Q4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다.
# 주민등록번호에서 성별을 나타내는 숫자를 출력해보자
# print(pin[7])

# Q5. 다음과 같은 문자열 a:b:C:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 출력.
# a = "a:b:c:d"
# b = a.replace(":","#")
# print(b)

#  Q6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자.
# a = [1, 3, 5, 4, 2]
# a. sort()
# a. reverse()
# print(a)

# Q7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# a = ['Life', 'is', 'too', 'short']
# result = " ".join(a)
# print(result)

# a = (1,  2, 3)
# a = a + (4,)
# print(a)

# Q10. 딕셔너리 a에서  'B'에 해당되는 값을 추출해 보자.
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a)
# print(result)

# Q11. a 리스트에서 중복 숫자를 제거해 보자.
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)
# b = list(aSet)
# print(b)

# a = b = [1, 2, 3]
# a[1] = 4
# print(b)