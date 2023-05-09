def f(m):
    res = 0
    for i in range(N):
        res += m % a[i]
    return res
N = int(input())
a = list(map(int, input().split()))
