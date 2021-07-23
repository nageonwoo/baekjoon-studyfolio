T=int(input())
for _ in range(T):
    stack=0
    ps=input()
    flag=True#for x in ps를 하면 stack이 음수되면 False
    for x in ps:
        if x =='(':stack+=1
        elif x ==')':stack-=1
        if stack<0:flag=False
    if flag and stack==0:print('YES')
    else:print('NO')

'''
1
(()())((()))
'''