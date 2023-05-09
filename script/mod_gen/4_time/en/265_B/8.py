def problem265_b():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(m):
        t = t - (x[i] - x[i-1]) - a[x[i]-2] + y[i]
        if t <= 0:
            print("No")
            exit()
    t = t - (n - x[m-1]) - a[n-2]
    if t <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    problem265_b()