#입력받은 정수까지의 짝수 합 구하기

a=int(input())
s=0

for i in range(1,a+1):
    if i%2==0:
        s+=i
    
print(s)

