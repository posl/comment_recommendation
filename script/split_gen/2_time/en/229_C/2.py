def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_b = max(B)
    if max_b > W:
        max_b = W
    max_dp = max_a * max_b
    dp = [0] * (max_dp + 1)
    for i in range(N):
        for j in range(max_dp, 0, -1):
            if j - A[i] * B[i] >= 0:
                dp[j] = max(dp[j], dp[j - A[i] * B[i]] + A[i])
    ans = 0
    for i in range(max_dp + 1):
        if i <= W:
            ans = max(ans, dp[i])
    print(ans)
