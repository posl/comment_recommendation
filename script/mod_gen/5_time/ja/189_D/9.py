def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    # dp[i][j] := i番目の演算子まででjがTrueとなるパターン数
    dp = [[0 for i in range(2)] for j in range(N+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1,N+1):
        if S[i-1] == "AND":
            dp[i][0] = dp[i-1][0] * 2 + dp[i-1][1]
            dp[i][1] = dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][0] + dp[i-1][1] * 2
    #print(dp)
    print(dp[N][1])

if __name__ == '__main__':
    main()