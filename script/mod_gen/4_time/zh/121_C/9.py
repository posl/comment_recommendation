def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    s = 0
    for i in range(n):
        s += b[i]
    if s <= m:
        print(sum(a))
    else:
        c = []
        for i in range(n):
            c.append(a[i]/b[i])
        c.sort()
        s = 0
        for i in range(n):
            s += b[i]
            if s >= m:
                break
        print(sum(c[:i+1])*m)

if __name__ == '__main__':
    main()