# stack은 후입선출
# queue는 선입선출

#stack 직접 구현

stack=[]
print(stack)

print('===== push =====')
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)

print('===== pop =====')
print(stack.pop())
print(stack)

print('===== cf) del =====')
#stack.pop() #del로 하는게 성능이 더 좋음
del stack[-1]
print(stack)

#peek==[...]==메서드가 아니다
#마지막거만 출력
#stack[...]