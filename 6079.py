# 1부터 더한 합이 입력한 정수보다 같거나 작을때까지만 계속 더하기

n=int(input())
sum=0

for i in range(1,n):
    sum += i
    if sum >= n:
        break

print(i)









