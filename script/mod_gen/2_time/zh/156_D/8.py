def f(x):
    return sum((a-x)**2 for a in A)
N = int(input())
A = list(map(int, input().split()))
print(min(f(x) for x in range(1,101)))
