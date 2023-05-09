def solve():
    n = int(input())
    a = [0] * n
    p = [0] * n
    x = [0] * n
    for i in range(n):
        a[i], p[i], x[i] = map(int, input().split())
    ans = 10**9
    for i in range(n):
        if x[i] > a[i]:
            ans = min(ans, p[i])
    if ans == 10**9:
        ans = -1
    print(ans)
