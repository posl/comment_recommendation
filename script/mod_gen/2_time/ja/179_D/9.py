def solve():
    # 標準入力
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    # ここに処理を記述
    # 1からNまでの数列を作成
    # DP[i] = iに移動する方法の総数
    DP = [0] * (N + 1)
    DP[1] = 1
    for i in range(2, N + 1):
        for LR in LRs:
            L, R = LR
            if i - L < 0:
                continue
            if i - R < 0:
                DP[i] += DP[i - L] % 998244353
            else:
                DP[i] += DP[i - L] - DP[i - R - 1] % 998244353
    print(DP[N] % 998244353)

if __name__ == '__main__':
    solve()