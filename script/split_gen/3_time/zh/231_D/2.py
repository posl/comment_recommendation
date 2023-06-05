def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for _ in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A,B)
    #print(A[0],B[0])
    #print(A[1],B[1])
    #print(A[2],B[2])
    #print(N,M)
    for i in range(1,N+1):
        #print(i)
        if i in A:
            #print("A")
            if i+1 in A:
                #print("A")
                return "No"
            else:
                #print("B")
                if i+1 in B:
                    #print("A")
                    return "No"
    return "Yes"
