def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 从左到右的累积和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 从左到右的累积和除以m的余数
    t = [0] * n
    for i in range(n):
        t[i] = s[i + 1] % m
    from collections import Counter
    c = Counter(t)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()