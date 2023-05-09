def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    l = 0
    r = 10**9
    while r - l > 10**(-6):
        m = (l + r) / 2
        if check(m, n, a, b):
            r = m
        else:
            l = m
    print(r)

if __name__ == '__main__':
    solve()