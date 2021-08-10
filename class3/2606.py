v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

start = 1
stack = [start]
visited = [False] * (v + 1)

# dfs
