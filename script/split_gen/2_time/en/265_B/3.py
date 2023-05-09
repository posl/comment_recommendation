def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    for i in range(N-1):
        T -= A[i]
        if T <= 0:
            print("No")
            return
        if i+1 in X:
            T += Y[X.index(i+1)]
            if T > M:
                T = M
    print("Yes")
