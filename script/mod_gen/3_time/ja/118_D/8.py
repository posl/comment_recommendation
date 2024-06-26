def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #dp[i]:整数iを作るために使うマッチ棒の本数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i - A[j] >= 0 and dp[i - A[j]] != -1:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)
    #dp[N]が-1の場合は作れない
    if dp[N] == -1:
        print(-1)
        return
    #dp[N]が0の場合は0しか作れない
    if dp[N] == 0:
        print(0)
        return
    #dp[N]が1以上の場合はdp[i]が最大のiを見つける
    #dp[1]が最大の場合は1を作れる
    #dp[2]が最大の場合は11を作れる
    #dp[3]が最大の場合は111を作れる
    #dp[4]が最大の場合は1111を作れる
    #dp[5]が最大の場合は11111を作れる
    #dp[6]が最大の場合は111111を作れる
    #dp[7]が最大の場合は1111111を作れる
    #dp[8]が最大の場合は11111111を作れる
    #dp[9]が最大の場合は111111111を作れる
    #dp[10]が最大の場合は1111111111を作れる
    #dp[11]が最大の場合は11111111111を作れる
    #dp[12]が最大の場合は111111111111を作れる
    #dp[13]が最大の場合は1111111111111を作れ

if __name__ == '__main__':
    main()