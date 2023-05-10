def main():
    L,Q = map(int,input().split())
    X = [0,L]
    C = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            idx = X.index(x)
            C.append(X[idx+1] - X[idx-1])
    C.sort()
    for i in range(1,Q+1):
        print(C[i])
