def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算前缀和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 计算答案
    ans = -(10 ** 18)
    for i in range(1, n + 1):
        if i - m >= 0:
            ans = max(ans, s[i] - s[i - m])
    print(ans)

if __name__ == '__main__':
    main()