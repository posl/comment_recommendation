def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    t = T
    p = 1
    for i in range(N-1):
        t = t - A[i]
        if t <= 0:
            print("No")
            return
        if p in X:
            t = min(T,t+Y[X.index(p)])
        p += 1
    print("Yes")
    return

if __name__ == '__main__':
    main()