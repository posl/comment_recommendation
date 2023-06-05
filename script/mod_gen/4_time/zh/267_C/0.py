def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 初始化
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    # 解决
    ans = -10 ** 18
    for i in range(m, n + 1):
        ans = max(ans, b[i] - b[i - m])
    print(ans)

if __name__ == '__main__':
    main()