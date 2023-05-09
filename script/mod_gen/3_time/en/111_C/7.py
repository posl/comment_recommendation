def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[::2]
    b = v[1::2]
    c = [0] * 10**5
    d = [0] * 10**5
    for i in a:
        c[i-1] += 1
    for j in b:
        d[j-1] += 1
    e = c.index(max(c))
    f = d.index(max(d))
    if e == f:
        g = c.index(sorted(c)[-2])
        h = d.index(sorted(d)[-2])
        print(min(n-c[e]-d[h], n-c[g]-d[f]))
    else:
        print(n-c[e]-d[f])

if __name__ == '__main__':
    main()