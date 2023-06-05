def solve():
    n,c = map(int, input().split())
    d = {}
    for _ in range(n):
        a,b,c = map(int, input().split())
        d[a] = d.get(a,0) + c
        d[b+1] = d.get(b+1,0) - c
    d = sorted(d.items())
    ans = 0
    s = 0
    t = 0
    for i in range(len(d)-1):
        s += d[i][1]
        t += d[i+1][0] - d[i][0]
        if s > c:
            ans += c * t
        else:
            ans += s * t
    print(ans)

if __name__ == '__main__':
    solve()