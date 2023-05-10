def main():
    N,M = list(map(int,input().split()))
    X = []
    Y = []
    Z = []
    for i in range(N):
        x,y,z = list(map(int,input().split()))
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = 0
    for i in range(2**3):
        Xp = []
        Yp = []
        Zp = []
        for j in range(3):
            if ((i >> j) & 1):
                Xp.append(X[j])
                Yp.append(Y[j])
                Zp.append(Z[j])
            else:
                Xp.append(-X[j])
                Yp.append(-Y[j])
                Zp.append(-Z[j])
        Xp.sort(reverse=True)
        Yp.sort(reverse=True)
        Zp.sort(reverse=True)
        ans = max(ans,sum(Xp[:M])+sum(Yp[:M])+sum(Zp[:M]))
    print(ans)
