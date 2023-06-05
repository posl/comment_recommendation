def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(N):
        if i == N - 1:
            res += a[i] - 1
        else:
            res += a[i] - 2
    print(res)
