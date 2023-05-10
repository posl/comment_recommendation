def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    max_w = W + 1
    dp = [[0 for i in range(max_w)] for j in range(N+1)]
    for i in range(N):
        for j in range(max_w):
            if j == 0:
                dp[i+1][j] = 1
            elif j >= A[i]:
                dp[i+1][j] = dp[i][j] or dp[i][j-A[i]]
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    ans = 0
    for i in range(max_w):
        if dp[N][i] == 1:
            ans += 1
    print(ans)
