def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    # 二分查找
    left = 0
    right = 10 ** 9
    while right - left > 1e-6:
        mid = (left + right) / 2
        # 计算灯光覆盖的区域
        light = []
        for i in range(k):
            light.append((x[a[i] - 1], y[a[i] - 1], mid))
        while True:
            flag = False
            for i in range(len(light)):
                for j in range(i + 1, len(light)):
                    if (light[i][0] - light[j][0]) ** 2 + (light[i][1] - light[j][1]) ** 2 < (light[i][2] + light[j][2]) ** 2:
                        flag = True
                        light[i] = (light[i][0], light[i][1], max(light[i][2], light[j][2]))
                        light.pop(j)
                        break
                if flag:
                    break
            if not flag:
                break
        if len(light) == 1:
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()