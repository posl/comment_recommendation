def main():
    n, c = map(int, input().split())
    a = []
    b = []
    d = []
    for i in range(n):
        a.append(0)
        b.append(0)
        d.append(0)
    for i in range(n):
        a[i], b[i], d[i] = map(int, input().split())
    s = 0
    e = 0
    p = 0
    for i in range(n):
        s = a[i]
        e = b[i] + 1
        p = d[i]
        d[i] = 0
        for j in range(s, e):
            d[j - 1] += p
    m = max(d)
    if m > c:
        print(c)
    else:
        print(m)

if __name__ == '__main__':
    main()