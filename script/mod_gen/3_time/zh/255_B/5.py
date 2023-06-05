def main():
    # 输入
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(n):
        xi,yi = map(int,input().split())
        x.append(xi)
        y.append(yi)
    # 答案
    ans = 0
    # 左右边界
    left = 0
    right = 100000000
    
    # 二分查找
    while right - left > 0.000000001:
        # 中间值
        mid = (left + right) / 2
        # 用mid的强度能否照亮所有人
        ok = False
        # 所有的人
        for i in range(n):
            # 最小强度
            min_r = 10000000000
            # 所有灯
            for j in range(k):
                # 灯与人的距离
                r = ((x[i] - x[a[j]-1]) ** 2 + (y[i] - y[a[j]-1]) ** 2) ** 0.5
                # 最小强度
                min_r = min(min_r,r)
            # 如果最小强度小于mid
            if min_r < mid:
                # 无法照亮所有人
                ok = False
                # 跳出循环
                break
            # 最小强度大于等于mid
            else:
                # 可以照亮所有人
                ok = True
        # 如果可以照亮所有人
        if ok:
            # 答案为mid
            ans = mid
            # 最小强度为mid
            left = mid
        # 如果无法照亮所有人
        else:
            # 最大强度为mid
            right = mid
    # 输出
    print(ans)

if __name__ == '__main__':
    main()