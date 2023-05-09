def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        x,y = map(int,input().split())
        X[i] = x
        Y[i] = y
    X.sort()
    Y.sort()
    x = [0]*(N+1)
    y = [0]*(N+1)
    for i in range(N):
        x[i+1] = x[i] + X[i]
        y[i+1] = y[i] + Y[i]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            x1 = X[i]
            x2 = X[j]
            y1 = Y[i]
            y2 = Y[j]
            ans += (i-x[i])*(y[N]-y[j]) + (x[j]-x[i])*(y[N]-y[j]) + (x[N]-x[j])*(j-y[j])
    print(ans)

if __name__ == '__main__':
    main()