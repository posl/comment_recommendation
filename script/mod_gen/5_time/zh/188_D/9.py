def solve():
    N, C = map(int, input().split())
    service = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        service.append((a, c))
        service.append((b + 1, -c))
    service.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in service:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)

if __name__ == '__main__':
    solve()