def main():
    # 读取输入
    n = int(input())
    d = list(map(int, input().split()))
    # 求和
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    # 输出
    print(sum)

if __name__ == '__main__':
    main()