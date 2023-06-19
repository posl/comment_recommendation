def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(m):
        if i == 0:
            if a[i] > 0.5:
                print('No')
                return
            else:
                n -= a[i]
                n += b[i] - a[i]
        else:
            n -= a[i] - b[i-1]
            n += b[i] - a[i]
        if n <= 0:
            print('No')
            return
    if t - b[m-1] <= 0.5:
        print('No')
        return
    else:
        n -= t - b[m-1]
        if n <= 0:
            print('No')
            return
        else:
            print('Yes')
            return

if __name__ == '__main__':
    main()