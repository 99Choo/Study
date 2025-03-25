c=input("반지름을 입력하세요")

c=int(c)

a=float(2*3.141592*c)
b=float(3.141592*c**2)


print("반지름이 %d인 원의 둘레는 : %f 입니다." %(c,a))
print("반지름이 %d인 원의 넓이는 : %f 입니다." %(c,b))
