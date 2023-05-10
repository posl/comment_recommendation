def score(A, N, Q, a, b, c, d):
    ans = 0
    for i in range(Q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            ans += d[i]
    return ans
