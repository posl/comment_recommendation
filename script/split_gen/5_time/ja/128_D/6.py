def problem128_d():
    n, k = map(int, input().split())
    vs = list(map(int, input().split()))
    ans = 0
    for l in range(min(n, k) + 1):
        for r in range(min(n, k) - l + 1):
            if l + r > k:
                continue
            values = vs[:l] + vs[n-r:]
            values.sort()
            for v in values[:k - l - r]:
                if v < 0:
                    values.remove(v)
            ans = max(ans, sum(values))
    print(ans)
