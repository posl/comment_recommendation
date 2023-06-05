def solve(N, W, A):
    A.sort()
    A = list(set(A))
    dp = [False] * (W + 1)
    dp[0] = True
    for i in range(len(A)):
        for j in range(W, -1, -1):
            if j - A[i] >= 0 and dp[j - A[i]]:
                dp[j] = True
    ans = 0
    for i in range(W + 1):
        if dp[i]:
            ans += 1
    return ans
