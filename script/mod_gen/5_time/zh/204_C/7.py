def problem204_c():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A = set(A)
    B = set(B)
    print(N-len(A&B))
problem204_c()
