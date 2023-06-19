def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [False] * (x + 1)
    dp[0] = True
    for i in range(n):
        for j in range(x + 1):
            if dp[j]:
                dp[j] = True
            elif j - a[i] >= 0 and dp[j - a[i]] and b[i] > 0:
                dp[j] = True
                b[i] -= 1
    if dp[x]:
        print('Yes')
    else:
        print('No')
