def problems278_a():
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = list(map(int,input().split()))
    #print(N, K, A)
    for i in range(K):
        A.pop(0)
        A.append(0)
    for i in range(N):
        if i == N-1:
            print(A[i])
        else:
            print(A[i], end=" ")
problems278_a()
