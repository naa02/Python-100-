#문자 1개 입력받아 a부터 그문자까지의 알파벳 출력하기

a=ord(input()) #끝점
t=ord('a') #시작점

while t<=a:
    print(chr(t),end=' ')
    t+=1
