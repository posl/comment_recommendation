def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            if j - a[i] >= 0:
                dp[i+1][j] += dp[i][j-a[i]]
            if j - b[i] >= 0:
                dp[i+1][j] += dp[i][j-b[i]]
    if dp[N][S] == 0:
        print("No")
    else:
        print("Yes")
        ans = []
        j = S
        for i in range(N, 0, -1):
            if dp[i-1][j-a[i-1]] == 1:
                ans.append("H")
                j -= a[i-1]
            else:
                ans.append("T")
                j -= b[i-1]
        print("".join(ans[::-1]))
