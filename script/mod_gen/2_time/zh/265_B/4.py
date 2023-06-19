def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    a.append(0)
    a.append(0)
    x.append(n)
    y.append(0)
    for i in range(m):
        a[x[i]-1] = a[x[i]-1] + y[i]
    for i in range(n-1):
        t = t - a[i]
        if t <= 0:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()