def main():
    # 输入
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    # 排序
    x.sort()
    # 计算每个点的距离
    diffs = []
    for i in range(m-1):
        diffs.append(x[i+1] - x[i])
    # 排序
    diffs.sort()
    # 计算总和
    sum = 0
    for i in range(m-n):
        sum += diffs[i]
    # 输出
    print(sum)

if __name__ == '__main__':
    main()