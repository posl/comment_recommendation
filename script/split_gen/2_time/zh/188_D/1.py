def main():
    N, C = map(int, input().split())
    d = []
    for i in range(N):
        a, b, c = map(int, input().split())
        d.append((a, c))
        d.append((b+1, -c))
    d.sort()
    ans = 0
    fee = 0
    t = 0
    for i in range(len(d)):
        if d[i][0] != t:
            ans += min(C, fee) * (d[i][0] - t)
            t = d[i][0]
        fee += d[i][1]
    print(ans)
