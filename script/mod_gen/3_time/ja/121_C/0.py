def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append((a[i], b[i]))
    c.sort()
    #print(c)
    ans = 0
    for i in range(n):
        if m >= c[i][1]:
            ans += c[i][0] * c[i][1]
            m -= c[i][1]
        else:
            ans += c[i][0] * m
            break
    print(ans)

if __name__ == '__main__':
    main()