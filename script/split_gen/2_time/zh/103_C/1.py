def f(m):
    result = 0
    for i in range(N):
        result += m % a[i]
    return result
N = int(input())
a = list(map(int, input().split()))
