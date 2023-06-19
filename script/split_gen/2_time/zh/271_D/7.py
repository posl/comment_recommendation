def solve():
    N, S = map(int, input().split())
    A = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append((a, b))
    dp = [[False for i in range(S + 1)] for j in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i][0]:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - A[i][0]]
            if j >= A[i][1]:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - A[i][1]]
    if not dp[N][S]:
        print("No")
        return
    print("Yes")
    ans = ""
    for i in range(N - 1, -1, -1):
        if S >= A[i][0] and dp[i][S - A[i][0]]:
            ans += "H"
            S -= A[i][0]
        else:
            ans += "T"
            S -= A[i][1]
    print(ans[::-1])
