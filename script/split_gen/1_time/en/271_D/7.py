def solve(N, S, A, B):
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            if j >= A[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-A[i]])
            if j >= B[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-B[i]])
    if dp[N][S] == 0:
        print("No")
    else:
        print("Yes")
        ans = ""
        for i in range(N):
            if S >= A[N-i-1] and dp[N-i-1][S-A[N-i-1]] == 1:
                ans += "H"
                S -= A[N-i-1]
            else:
                ans += "T"
                S -= B[N-i-1]
        print(ans)
