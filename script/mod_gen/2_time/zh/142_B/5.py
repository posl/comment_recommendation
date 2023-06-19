def main():
    # 读取数据
    N, K = map(int, input().split())
    h = [int(i) for i in input().split()]
    # 计算
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()