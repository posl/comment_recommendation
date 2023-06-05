def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 累加求和
    sum = 0
    for i in range(4 * n - 1):
        sum += a[i]
    # 计算答案
    ans = sum // (n * 2) - sum // (n * 4)
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()