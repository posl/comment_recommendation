def get_input():
    N,M,K = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    C = []
    D = []
    for i in range(K):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)
    return N,M,K,A,B,C,D
