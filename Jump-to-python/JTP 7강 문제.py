# Q1. split와 join 함수를 사용하여 위 문자열 고치기
# a:b:c:d -> a#b#c#d
# e = "a:b:c:d"

# d = e.split(":")

# result = "#".join(d)
# print(result)

# Q2 딕셔너리 a에서 'C'라는 key에 대항다는 value를 출력하는 프로그램.
# a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다. 'C'에 해당하는 key 값이 없을 경우
# 오류 대신 70을 얻을 수 있도록 수정하시오.

# a = {'A':90, 'B':80}
# print(a.get("C", 70))

# 리스트 a가 있다. 리스트 a에[4,5]를 + 기호를 사용하여 더한 결과는 다음과 같다.
# a = [1, 2, 3]
# a = a + [4,5]
# print(a)

# a = [1, 2, 3]
# a. extend([4,5])
# print(a)

# +기호를 사용하여 더한 것과 extend한 것의 차이점을 설명하시오.
# extedn은 원본이 수정되고 +는 원본이 수정되지 않는다.

# Q4. 50점 이상 점수의 총합을 구하시오.
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25] 
# result = 0
# for i in A:
    #   if i >= 50:
        # result += i
# print(result)

# 숫자의 총합을 구하는 프로그램을 작성하시오.
# A = [65, 45, 2, 3, 45, 8]
# result = 0
# for i in A:
#     result += i
# print(result)



# a = input("숫자를 입력하세요")
# b = a.split(",")
# total = 0
# for c in b:
    # total += int(c)
# print(total)

# n = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
# for i in range(1, 10):
    # print(n*i) 
