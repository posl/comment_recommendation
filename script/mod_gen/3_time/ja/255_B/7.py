def main():
    import sys
    from math import sqrt
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    # 人iの明かりの強さを求める
    def calc_r(i):
        r = 0
        for j in range(N):
            if i == j:
                continue
            r = max(r, sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) / 2)
        return r
    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]
    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]
    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]
    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]
    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]
    # 人iが明かりjによって照らされるかどうか

if __name__ == '__main__':
    main()