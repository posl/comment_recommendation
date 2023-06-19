def main():
    # 读取输入
    a = list(map(int, input().split()))
    # 初始化
    ans = 10000000000
    # 遍历所有情况
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # 计算总成本
                sum = abs(a[0] - a[i]) + abs(a[1] - a[j]) + abs(a[2] - a[k])
                # 更新最小总成本
                ans = min(ans, sum)
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()