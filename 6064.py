#6064번 정수 3개 입력받아 가장 작은 값 출력하기

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

small=(a if a<b else b) if ((a if a<b else b)<c) else c
print(small)




