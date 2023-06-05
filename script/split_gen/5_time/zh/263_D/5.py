def minsum(N, L, R, A):
    ans = 0
    for i in range(N):
        if A[i] > 0:
            ans += A[i] * R
        else:
            ans += A[i] * L
    return ans
