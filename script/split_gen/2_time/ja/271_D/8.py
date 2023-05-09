def main():
    N, S = map(int, input().split())
    A = [0 for i in range(N)]
    B = [0 for i in range(N)]
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    dp = [[False for i in range(S+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            dp[i+1][j] = dp[i][j]
            if j >= A[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-A[i]]
            if j >= B[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-B[i]]
    if dp[N][S]:
        print("Yes")
        ans = ["" for i in range(N)]
        i = N
        j = S
        while i > 0:
            if j >= A[i-1] and dp[i-1][j-A[i-1]]:
                ans[i-1] = "H"
                j -= A[i-1]
            else:
                ans[i-1] = "T"
                j -= B[i-1]
            i -= 1
        print("".join(ans))
    else:
        print("No")
