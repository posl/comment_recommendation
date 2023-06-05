def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    s = set(c[:k])
    ans = len(s)
    for i in range(k, n):
        s.add(c[i])
        s.discard(c[i - k])
        ans = max(ans, len(s))
    print(ans)
solve()
