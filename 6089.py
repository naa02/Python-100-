#등비수열 출력하기
#a:시작 값, r:등비, n:몇번째인지
a,r,n=input().split()
a=int(a)
r=int(r)
n=int(n)

print(a*(r**(n-1)))
