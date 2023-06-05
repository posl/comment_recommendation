def solve(K, N, A):
    A.sort()
    ret = K
    for i in range(N):
        if i == N-1:
            ret = min(ret, K-A[i]+A[0])
        else:
            ret = min(ret, A[i+1]-A[i])
    return ret
