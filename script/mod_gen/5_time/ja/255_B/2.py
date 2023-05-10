def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #print(N, K)
    #print(A)
    #print(X)
    #print(Y)
    # 人数が1人の場合
    if N == 1:
        print(0)
        exit()
    # 人数が2人の場合
    if N == 2:
        x0 = X[0]
        y0 = Y[0]
        x1 = X[1]
        y1 = Y[1]
        if x0 == x1 and y0 == y1:
            print(0)
            exit()
        else:
            print(((x0 - x1)**2 + (y0 - y1)**2)**(1/2))
            exit()
    # 人数が3人以上の場合
    # 人iの座標を(x_i, y_i)とする
    # 人iが明かりを持つ場合、明かりの強さをR_iとする
    # 人iの明かりによって人jが照らされる場合、
    # (x_i - x_j)^2 + (y_i - y_j)^2 <= R_i^2
    # が成り立つ
    # これをすべてのi, jについて考えると、
    # 人iの明かりの強さをR_iとするとき、
    # R_i^2 >= max{(x_i - x_j)^2 + (y_i - y_j)^2 | j = 1, 2, ..., N}
    # となる必要がある
    # すべての人が少なくとも1つの明かりによって照らされるために必要な明かりの強さの最小値は、
    # R = max{R_i | i = 1, 2, ..., K}

if __name__ == '__main__':
    main()