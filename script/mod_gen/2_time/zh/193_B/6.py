def solve():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min_price = 10**9
    for i in range(n):
        if x[i] > 0:
            min_price = min(min_price, p[i])
    if min_price == 10**9:
        print(-1)
        return
    print(min_price)

if __name__ == '__main__':
    solve()