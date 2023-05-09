def main():
    #入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #初期化
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                if dp[i - A[j]] == 0:
                    dp[i] = 1
                    break
                else:
                    dp[i] = 0
    print(dp[N])

if __name__ == '__main__':
    main()