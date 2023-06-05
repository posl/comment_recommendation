def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    for i in range(m):
        if t + a[i] >= x[i]:
            t = t + a[i] + y[i]
        else:
            print("No")
            exit()
    if t >= n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()