def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for _ in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    time = t
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print("No")
            exit()
        if (i+1) in x:
            time += y[x.index(i+1)]
            if time > t:
                time = t
    print("Yes")
