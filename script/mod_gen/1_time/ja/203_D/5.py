def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    # 二次元累積和
    # dp[i][j] = A[0][0] + ... + A[i-1][j-1]
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + A[i][j]
    # 二分探索
    def check(x):
        for i in range(N-K+1):
            for j in range(N-K+1):
                if dp[i+K][j+K] - dp[i+K][j] - dp[i][j+K] + dp[i][j] >= x:
                    return True
        return False
    # 答えの候補は0以上10**9以下なので、二分探索で探す
    ok = 0
    ng = 10**9+1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()