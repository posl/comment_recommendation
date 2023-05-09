def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        if m > 0:
            if b[i] <= m:
                ans += a[i]*b[i]
                m -= b[i]
            else:
                ans += a[i]*m
                m = 0
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()