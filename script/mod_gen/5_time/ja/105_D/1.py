def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 1 から n までの累積和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # s[r] - s[l] が m の倍数となる組 (l, r) を求める
    # その個数を ans に加算する
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for r in range(n + 1):
        ans += d[s[r] % m]
        d[s[r] % m] += 1
    print(ans)
solve()

if __name__ == '__main__':
    solve()