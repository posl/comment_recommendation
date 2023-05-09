def main():
    import sys
    from math import sqrt
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    from scipy.sparse import csr_matrix
    readline = sys.stdin.readline
    N = int(readline())
    sx, sy, tx, ty = map(int, readline().split())
    X = np.zeros((N, 2), dtype=np.int64)
    R = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x, y, r = map(int, readline().split())
        X[i] = np.array([x, y])
        R[i] = r
    # 2点間の距離
    def dist(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)
    # 2点間の距離がr1+r2以下かどうか
    def is_ok(x1, y1, r1, x2, y2, r2):
        return dist(x1, y1, x2, y2) <= r1+r2
    # 2点間の距離がr1+r2以下なら1, そうでなければINF
    def weight(x1, y1, r1, x2, y2, r2):
        return 1 if is_ok(x1, y1, r1, x2, y2, r2) else float('inf')
    # 2点間の距離がr1+r2以下なら1, そうでなければ0
    def weight2(x1, y1, r1, x2, y2, r2):
        return 1 if is_ok(x1, y1, r1, x2, y2, r2) else 0
    # 隣接行列
    W = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            W[i, j] = weight2(X[i, 0], X[i, 1], R[i], X[j, 0], X[j, 1], R[j])
    # 隣接行列から最
