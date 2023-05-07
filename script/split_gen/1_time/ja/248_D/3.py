def solve():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    L = []
    R = []
    X = []
    for i in range(Q):
        l,r,x = map(int,input().split())
        L.append(l)
        R.append(r)
        X.append(x)
    #print(N,A,Q,L,R,X)
    for i in range(Q):
        print(A[L[i]-1:R[i]].count(X[i]))
