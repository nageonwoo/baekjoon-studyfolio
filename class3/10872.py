import sys
sys.setrecursionlimit(1003)

def factorial(n):
    if n == 0: return 1
    elif n >= 0: return n * factorial(n-1)

print(factorial(0))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(1000))