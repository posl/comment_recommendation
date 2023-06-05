def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    l.sort()
    r.sort()
    print(max(0, min(r) - max(l) + 1))
