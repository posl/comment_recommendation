def main():
    N, S = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - A[i]]
            if j - B[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - B[i]]
    if dp[N][S]:
        print("Yes")
        ans = ""
        for i in reversed(range(N)):
            if S - A[i] >= 0 and dp[i][S - A[i]]:
                ans += "H"
                S -= A[i]
            else:
                ans += "T"
                S -= B[i]
        print(ans[::-1])
    else:
        print("No")
