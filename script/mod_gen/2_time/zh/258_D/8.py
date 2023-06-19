def main():
    # 读入数据
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # 二分查找
    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        # 判断mid分钟内能否清除x个阶段
        cnt = 0
        for i in range(n):
            # 如果mid分钟内能清除第i个阶段
            if a[i] <= mid:
                cnt += (mid - a[i]) // b[i] + 1
        if cnt >= x:
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()