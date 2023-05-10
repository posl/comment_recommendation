def solve(N, A):
    #print(N, A)
    maxA = 0
    for i in range(N):
        A[i] = A[i] % 360
        maxA = max(maxA, A[i])
    #print(A)
    A.sort()
    #print(A)
    maxA = max(maxA, 360-A[N-1]+A[0])
    for i in range(1, N):
        maxA = max(maxA, A[i]-A[i-1])
    return 360-maxA
