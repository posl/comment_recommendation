def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if n == 1:
        print(0)
        return
    if m == 1:
        print(0)
        return
    if m == 2:
        if n == 2:
            print(1)
            return
        print(0)
        return
    b = []
    for i in range(n):
        if i == 0:
            b.append(a[i])
        else:
            if a[i] == a[i-1]:
                continue
            b.append(a[i])
    #print(b)
    c = []
    for i in range(len(b)):
        if i == 0:
            c.append(b[i])
        else:
            c.append(b[i]-b[i-1])
    #print(c)
    d = []
    for i in range(len(b)):
        if i == 0:
            d.append(c[i])
        else:
            d.append(c[i]+d[i-1])
    #print(d)
    ans = 0
    for i in range(len(d)):
        if i == 0:
            ans += d[i]
        else:
            if d[i] == d[i-1]:
                continue
            ans += d[i]
    print(ans)
    return

if __name__ == '__main__':
    main()