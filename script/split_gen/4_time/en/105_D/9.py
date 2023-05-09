def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    from collections import Counter
    c = Counter()
    c[0] = 1
    s = 0
    for a in A:
        s = (s + a) % M
        c[s] += 1
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)
