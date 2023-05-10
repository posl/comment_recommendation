def main():
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = list(set(a))
    d = list(set(b))
    c.sort()
    d.sort()
    cdi = {}
    for i in range(len(c)):
        cdi[c[i]] = i + 1
    for i in range(len(d)):
        cdi[d[i]] = i + 1
    for i in range(len(a)):
        print(cdi[a[i]], cdi[b[i]])

if __name__ == '__main__':
    main()