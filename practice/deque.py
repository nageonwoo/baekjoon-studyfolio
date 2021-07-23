from collections import deque

stack = deque() # 빈 덱 선언
print(stack)

print("===== stack & queue =====")
stack = deque([1])
queue = deque([1])
print(stack)
print(queue)
print("=== push ===")
stack.append(2)
queue.append(2)
print(stack)
print(queue)
print("=== *peek ===")
print(stack[-1])
print(queue[0])
print("=== *pop ===")
print(stack.pop())
print(queue.popleft())
print(stack)
print(queue)