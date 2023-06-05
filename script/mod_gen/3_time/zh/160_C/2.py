def main():
    # 读入数据
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算最短距离
    min_dist = k
    for i in range(n):
        dist = k - a[i]
        if i == n - 1:
            dist += a[0]
        else:
            dist += a[i + 1]
        if dist < min_dist:
            min_dist = dist
    # 打印结果
    print(min_dist)

if __name__ == '__main__':
    main()