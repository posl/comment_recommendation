def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    z = []
    w = []
    for i in range(n):
        if i == 0:
            x.append(a[i])
        else:
            x.append(x[i-1]+a[i])
    for i in range(n):
        if i == 0:
            y.append(a[i])
        elif i == 1:
            y.append(y[i-1]+a[i])
        else:
            y.append(y[i-1]+a[i])
    for i in range(n):
        if i == 0:
            z.append(a[i])
        elif i == 1:
            z.append(z[i-1]+a[i])
        elif i == 2:
            z.append(z[i-1]+a[i])
        else:
            z.append(z[i-1]+a[i])
    for i in range(n):
        if i == 0:
            w.append(a[i])
        elif i == 1:
            w.append(w[i-1]+a[i])
        elif i == 2:
            w.append(w[i-1]+a[i])
        elif i == 3:
            w.append(w[i-1]+a[i])
        else:
            w.append(w[i-1]+a[i])
    for i in range(n):
        if x[i] == p and y[i] == q and z[i] == r:
            print('Yes')
            break
        elif i == n-1:
            print('No')

if __name__ == '__main__':
    main()