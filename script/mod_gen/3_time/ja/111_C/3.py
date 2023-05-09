def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[0::2]
    b = v[1::2]
    a.sort()
    b.sort()
    a.append(-1)
    b.append(-1)
    a.append(1000001)
    b.append(1000001)
    c = [a[0], a[1]]
    d = [b[0], b[1]]
    for i in range(2, n):
        if a[i] != a[i - 1]:
            c.append(a[i])
        if b[i] != b[i - 1]:
            d.append(b[i])
    if len(c) >= 4:
        c1 = c[0]
        c2 = c[1]
        c3 = c[2]
        c4 = c[3]
    else:
        c1 = c[0]
        c2 = c[1]
        c3 = c[1]
        c4 = c[1]
    if len(d) >= 4:
        d1 = d[0]
        d2 = d[1]
        d3 = d[2]
        d4 = d[3]
    else:
        d1 = d[0]
        d2 = d[1]
        d3 = d[1]
        d4 = d[1]
    if c1 == c2 and c3 == c4:
        if d1 == d2 and d3 == d4:
            print(min(n - c.count(c1) - d.count(d1), n - c.count(c3) - d.count(d3)))
        else:
            print(n - c.count(c1) - d.count(d1))
    elif d1 == d2 and d3 == d4:
        print(n - c.count(c3) - d.count(d3))
    else:
        print(n - c.count(c1) - d.count(d1) + n - c.count(c3) - d.count(d3))

if __name__ == '__main__':
    main()