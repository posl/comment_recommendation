def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
