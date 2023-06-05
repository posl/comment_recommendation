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
    # 二分搜索
    left = 0
    right = 10 ** 9
    while right - left > 10 ** -6:
        mid = (left + right) / 2
        # 使得灯光强度为mid时，能够照亮的人的编号
        lighted = []
        for i in range(k):
            lighted.append(a[i])
        for i in range(n):
            if i not in lighted:
                for j in range(len(lighted)):
                    if (x[i] - x[lighted[j]]) ** 2 + (y[i] - y[lighted[j]]) ** 2 <= mid ** 2:
                        lighted.append(i)
                        break
        if len(lighted) == n:
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()