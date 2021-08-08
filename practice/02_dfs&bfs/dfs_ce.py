# counter example

v = 3
e = 3
graph = [[], [2, 3], [1, 3], [1, 2]]
start = 1

# 0. 방문확인 1. 넣고 2. 빼고+이동 3. 방문체크
stack = [start] # 1. 넣고
visited = [False] * (v + 1)

while stack:
    now = stack.pop() # 2. 빼고+이동
    if visited[now] == True: continue # +. cycle
    print(now)
    visited[now] = True # 3. 방문체크
    for next in graph[now][::-1]:
        if visited[next] == True: continue # 0. 방문확인
        stack.append(next) # 1. 넣고