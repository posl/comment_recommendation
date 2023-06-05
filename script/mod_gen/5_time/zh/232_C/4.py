def main():
    n, m = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(m):
        c_i, d_i = map(int, input().split())
        c.append(c_i)
        d.append(d_i)
    aoki = []
    for i in range(n):
        aoki.append(i+1)
    high = []
    for i in range(n):
        high.append(i+1)
    for i in range(m):
        high[a[i]-1], high[b[i]-1] = high[b[i]-1], high[a[i]-1]
    for i in range(m):
        if aoki[c[i]-1] != high[c[i]-1] or aoki[d[i]-1] != high[d[i]-1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()