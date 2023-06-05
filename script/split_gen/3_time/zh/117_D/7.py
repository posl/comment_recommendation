def f(x):
    return sum([x^a for a in A])
N, K = map(int, input().split())
A = list(map(int, input().split()))
