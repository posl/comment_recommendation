def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    # 二分探索
    l = 0
    r = 10 ** 10
    while r - l > 10 ** -5:
        mid = (l + r) / 2
        # 人iが明かりjに照らされているか
        is_light = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= mid ** 2:
                    is_light[i][j] = 1
        # 人iが少なくとも1つの明かりに照らされているか
        is_lighted = [0] * N
        for i in range(N):
            for j in range(N):
                if is_light[i][j] == 1:
                    is_lighted[i] = 1
        # 人iが少なくとも1つの明かりに照らされている人の数
        lighted_num = 0
        for i in range(N):
            if is_lighted[i] == 1:
                lighted_num += 1
        if lighted_num >= N - K:
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()