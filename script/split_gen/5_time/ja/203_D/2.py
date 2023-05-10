def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 二次元累積和
    S = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + A[i][j]
    def get_sum(x1, y1, x2, y2):
        return S[x2][y2] - S[x1][y2] - S[x2][y1] + S[x1][y1]
    # 区画の左上のマスを(i, j)とする
    ans = float("inf")
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            # 区画の右下のマスを(i + K, j + K)とする
            # (i, j)から(i + K, j + K)までの区画の和を求める
            sum_ = get_sum(i, j, i + K, j + K)
            # 区画のマスの数が奇数の場合、マスの高さの中央値は区画のマスの数の半分+1番目に高いマスの高さとなる
            # 区画のマスの数が偶数の場合、マスの高さの中央値は区画のマスの数の半分番目と半分+1番目の高いマスの高さの平均となる
            # ここでは、区画のマスの数が奇数の場合も偶数の場合も同じように扱うため、(K^2 + 1) / 2番目に高いマスの高さとする
            # (K^2 + 1) / 2番目に高いマスの高
