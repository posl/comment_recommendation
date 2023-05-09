def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    l.sort()
    r.sort()
    ans = 0
    for i in range(1, n+1):
        if l[-1] <= i and i <= r[0]:
            ans += 1
    print(ans)
