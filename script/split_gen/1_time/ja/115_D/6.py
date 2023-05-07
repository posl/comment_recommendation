def solve(N, X):
    # レベル N のバーガーの層の数
    n = 2 ** (N + 1) - 3
    # レベル N のバーガーの下から X 層に含まれるパティの枚数
    # 1. レベル N のバーガーの一番下の層はバン
    # 2. レベル N のバーガーの下から X 層に含まれるパティの枚数は、
    #    レベル N-1 のバーガーの下から X-1 層に含まれるパティの枚数と等しい
    if X == 1:
        return 0
    elif X <= n + 1:
        return solve(N - 1, X - 1)
    elif X == n + 2:
        return 2 ** N - 1
    elif X <= 2 * n + 2:
        return 2 ** N - 1 - solve(N - 1, 2 * n + 3 - X)
    elif X == 2 * n + 3:
        return 2 ** N - 1
N, X = map(int, input().split())
print(solve(N, X))
