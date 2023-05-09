def problem():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A = sorted(A)
    #print(A)
    result = 0
    for i in range(K+1):
        #print(A[i], A[i+1])
        result += (A[i+1] - A[i] - 1) // (i+1)
    print(result)
