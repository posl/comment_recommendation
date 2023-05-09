def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    # 0-indexed
    a = [0] + a
    # 累積和
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        # 剰余を取る
        a[i] %= m
    # 剰余が同じものがあれば、その間の和はmの倍数
    # 1-indexed
    d = {}
    for i in range(1, n + 1):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    # 2つの選び方
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()