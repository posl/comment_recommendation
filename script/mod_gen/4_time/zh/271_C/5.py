def main():
    # 读取数据
    n = int(input())
    a = list(map(int, input().split()))
    # 从小到大排序
    a.sort()
    # 记录最大值
    ans = 0
    # 从大到小遍历
    for i in range(n-1, -1, -1):
        # 当前值大于最大值时
        if a[i] >= ans + 1:
            # 最大值加1
            ans += 1
        else:
            # 否则退出循环
            break
    # 输出最大值
    print(ans)

if __name__ == '__main__':
    main()