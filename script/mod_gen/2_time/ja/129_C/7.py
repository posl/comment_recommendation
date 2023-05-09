def main():
    #入力
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    #初期化
    mod = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    #計算
    for i in range(1, N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]+dp[i-2]
            dp[i] %= mod
    #出力
    print(dp[N])

if __name__ == '__main__':
    main()