def main():
    #input
    N, Q = map(int, input().split())
    L = [0]*N
    A = []
    for i in range(N):
        L[i] = int(input().split()[0])
        A.append(list(map(int, input().split())))
    SQ = [0]*Q
    TQ = [0]*Q
    for i in range(Q):
        SQ[i], TQ[i] = map(int, input().split())
    
    #compute
    #cumsum
    cums = [0]*N
    cums[0] = L[0]
    for i in range(1, N):
        cums[i] = cums[i-1] + L[i]
    
    #output
    for i in range(Q):
        if SQ[i] == 1:
            print(A[0][TQ[i]-1])
        else:
            print(A[SQ[i]-1][TQ[i]-1-cums[SQ[i]-2]])

if __name__ == '__main__':
    main()