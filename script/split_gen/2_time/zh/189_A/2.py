def solve():
    N,C = map(int, input().split())
    a = [0] * N
    b = [0] * N
    c = [0] * N
    for i in range(N):
        a[i], b[i], c[i] = map(int, input().split())
    # print(a,b,c)
    # print(N,C)
    # print(a)
    # print(b)
    # print(c)
    # print()
    # print()
    # print()
    # print()
    # dp[i] 表示第i天的最小花费
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + C
        for j in range(N):
            if i < a[j]:
                dp[i] += c[j]
            elif a[j] <= i <= b[j]:
                dp[i] += min(c[j], dp[a[j]-1] + (i-a[j]+1)*C)
    # print(dp)
    print(dp[N])
