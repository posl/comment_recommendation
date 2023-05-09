def f(m):
    return sum(m % a for a in A)
N = int(input())
A = list(map(int, input().split()))
