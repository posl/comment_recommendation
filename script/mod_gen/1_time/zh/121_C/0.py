def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ta,tb = map(int,input().split())
        a.append(ta)
        b.append(tb)
    ans = 0
    for i in range(n):
        if m <= b[i]:
            ans += a[i] * m
            break
        else:
            ans += a[i] * b[i]
            m -= b[i]
    print(ans)

if __name__ == '__main__':
    main()