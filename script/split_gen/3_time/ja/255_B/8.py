def main():
    import sys
    import math
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # 二分探索
    l = 0
    r = 10**10
    while r - l > 10**(-5):
        m = (l + r) / 2
        # 人iが明かりjに照らされているかの二次元配列
        light = [[False] * K for _ in range(N)]
        for i in range(N):
            for j in range(K):
                if (X[i] - X[A[j] - 1])**2 + (Y[i] - Y[A[j] - 1])**2 <= m**2:
                    light[i][j] = True
        # 人iが照らされている明かりの数
        light_num = [0] * N
        for i in range(N):
            for j in range(K):
                if light[i][j]:
                    light_num[i] += 1
        # 人iが照らされている明かりの数が0の人がいるか
        flag = False
        for i in range(N):
            if light_num[i] == 0:
                flag = True
        if flag:
            l = m
        else:
            r = m
    print(l)
