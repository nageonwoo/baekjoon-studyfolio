N= int(input())
for _ in range(N):
    ox=input()
    sum=0
    cnt=0
    for x in ox:
        if x=='O':cnt +=1
        elif x=='X':cnt = 0
        sum+=cnt
    print(sum)