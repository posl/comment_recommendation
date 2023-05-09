def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 二次元累積和
    S = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + A[i][j]
    # 二分探索
    def is_ok(x):
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if S[i + K][j + K] - S[i + K][j] - S[i][j + K] + S[i][j] >= x:
                    return True
        return False
    ng = -1
    ok = 10 ** 9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
