def main():
    N,M = map(int,input().split())
    X = []
    Y = []
    Z = []
    for i in range(N):
        x,y,z = map(int,input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = -1
    for i in range(2**3):
        sign = [1]*3
        for j in range(3):
            if i&(1<<j):
                sign[j] = -1
        tmp = []
        for j in range(N):
            tmp.append(sign[0]*X[j]+sign[1]*Y[j]+sign[2]*Z[j])
        tmp.sort(reverse=True)
        ans = max(ans,sum(tmp[:M]))
    print(ans)

if __name__ == '__main__':
    main()