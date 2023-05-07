def main():
    # 入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    # 処理
    # 2次元配列にする
    A2 = [[0 for i in range(N+1)] for j in range(10**9+1)]
    for i in range(N):
        A2[A[i]][i+1] = 1
    # 累積和をとる
    for i in range(10**9+1):
        for j in range(N):
            A2[i][j+1] += A2[i][j]
    # 出力
    for i in range(Q):
        if A2[X[i]][N] < K[i]:
            print(-1)
        else:
            left = 0
            right = N
            while right - left > 1:
                mid = (left + right) // 2
                if A2[X[i]][mid] >= K[i]:
                    right = mid
                else:
                    left = mid
            print(right)
