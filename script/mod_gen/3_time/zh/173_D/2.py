def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 按照顺序到达的玩家的舒适度
    b = [0] * n
    # 反向到达的玩家的舒适度
    c = [0] * n
    # 累加和
    for i in range(n):
        b[(i + 1) % n] += a[i]
        c[(i - 1) % n] += a[i]
    # 最大值
    for i in range(1, n):
        b[i] = max(b[i - 1], b[i])
        c[n - i - 1] = max(c[n - i], c[n - i - 1])
    # 输出
    for i in range(n):
        print(max(b[i], c[i]))

if __name__ == '__main__':
    main()