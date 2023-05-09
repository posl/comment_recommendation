def main():
    N = int(input())
    trampolines = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    # 二分探索
    def check(m):
        # 頂点を消す
        edges = []
        for i in range(N):
            x_i, y_i, p_i = trampolines[i]
            edges.append((i, N, max(0, p_i*m - abs(x_i) - abs(y_i))))
        # 頂点間の距離を計算
        for i in range(N):
            x_i, y_i, p_i = trampolines[i]
            for j in range(i+1, N):
                x_j, y_j, p_j = trampolines[j]
                edges.append((i, j, max(0, p_j*m - abs(x_i - x_j) - abs(y_i - y_j))))
        # ベルマンフォード法
        d = [float("inf")] * (N+1)
        d[N] = 0
        for _ in range(N):
            for i, j, c in edges:
                if d[i] > d[j] + c:
                    d[i] = d[j] + c
        return d[0] <= 0
    # 二分探索
    left = 0
    right = 10**18+1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()