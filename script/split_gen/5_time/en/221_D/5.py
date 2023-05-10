def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    m = max(a) + max(b)
    c = [0] * m
    for i in range(n):
        c[a[i]-1] += 1
        c[a[i]+b[i]-1] -= 1
    for i in range(1, m):
        c[i] += c[i-1]
    print(*c[:n])
solve()
