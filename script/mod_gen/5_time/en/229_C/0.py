def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N, W)
    dp = [[0 for i in range(3*10**5+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(3*10**5+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    ans = 0
    for i in range(3*10**5+1):
        if i <= W:
            ans = max(ans, dp[N][i])
    print(ans)

if __name__ == '__main__':
    main()