import sys
from collections import deque

N = int(sys.stdin.readline())
stack =deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "pop":
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif cmd[0] == "size": print(len(stack))
    elif cmd[0] == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
    elif cmd[0] == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
    elif cmd[0] == "push": stack.append(cmd[1])

#deque을 stack처럼 사용...다 똑같음
#push==append
#pop==popleft
#peek==queue