def problems127_d():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    BC = [list(map(int,input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1],reverse=True)
    i = 0
    j = 0
    while j<M and i<N and BC[j][1]>A[i]:
        A[i] = BC[j][1]
        BC[j][0] -= 1
        if BC[j][0]==0:
            j += 1
        i += 1
    print(sum(A))
