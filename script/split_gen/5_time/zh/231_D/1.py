def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A,B)
    #print(N,M)
    #print(N-1)
    #print(A.count(1))
    if N == 1:
        print("Yes")
        return
    if N-1 == A.count(1):
        print("Yes")
        return
    print("No")
    return
