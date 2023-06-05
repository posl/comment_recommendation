def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & 1:
                cnt += 1
            a[j] >>= 1
        ans += cnt * (n - cnt) * pow(2, i, mod)
        ans %= mod
    print(ans)
solve()
