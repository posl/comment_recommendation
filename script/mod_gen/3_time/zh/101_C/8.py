def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k, a)
    # 初始化
    ans = 0
    # 遍历，找到最小值
    for i in range(n):
        ans += 1
        # 如果最小值是在最后的k个数里，那么就不用再往后找了
        if i + k - 1 >= n:
            break
        # 找到最小值
        min_num = a[i]
        # 遍历，找到最小值
        for j in range(k):
            if a[i + j] < min_num:
                min_num = a[i + j]
        # 替换
        for j in range(k):
            a[i + j] = min_num
    # 输出
    print(ans)

if __name__ == '__main__':
    main()