def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    now = n
    for i in range(m):
        if i == 0:
            now -= a[i]
        else:
            now -= a[i] - b[i-1]
        if now <= 0:
            print('No')
            return
        now += b[i] - a[i]
        if now >= n:
            now = n
    now -= t - b[-1]
    if now <= 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()