def get_input():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a,p,x = map(int,input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    return N,A,P,X
