def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    # 二分法
    ok = 0
    ng = 100000000
    while ng - ok > 1e-6:
        mid = (ok + ng) / 2
        # 灯的坐标
        ax = [0] * k
        ay = [0] * k
        for i in range(k):
            ax[i] = x[a[i] - 1]
            ay[i] = y[a[i] - 1]
        # 求最小圆
        ok2 = 0
        ng2 = 100000000
        while ng2 - ok2 > 1e-6:
            mid2 = (ok2 + ng2) / 2
            # 判断是否所有人都被灯照亮
            ok3 = False
            for i in range(n):
                ok4 = False
                for j in range(k):
                    if (x[i] - ax[j]) ** 2 + (y[i] - ay[j]) ** 2 <= mid ** 2:
                        ok4 = True
                if not ok4:
                    ok3 = True
            if ok3:
                ok2 = mid2
            else:
                ng2 = mid2
        if ok2 <= mid:
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()