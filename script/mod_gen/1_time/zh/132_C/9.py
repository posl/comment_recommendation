def main():
    # 读取输入
    N = int(input())
    d = list(map(int, input().split()))
    # 求和
    s = sum(d)
    # 累积和
    a = [0] * (N + 1)
    for i in range(N):
        a[i + 1] = a[i] + d[i]
    # 确定最小值
    m = 10**9
    for i in range(1, N + 1):
        m = min(m, abs(s - 2 * a[i]))
    # 计数
    ans = 0
    for i in range(1, N + 1):
        if abs(s - 2 * a[i]) == m:
            ans += 1
    # 输出
    print(ans)

if __name__ == '__main__':
    main()