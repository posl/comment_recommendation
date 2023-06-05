def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n-1):
        t = t - a[i]
        if (i+1) in x:
            t = t + y[x.index(i+1)]
        if t <= 0:
            print("No")
            break
        if i == n-2:
            print("Yes")
main()
