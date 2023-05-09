def solve(N, K, A):
    #print(N, K, A)
    s = 0
    l = 0
    r = 0
    ans = 0
    while r < N:
        s += A[r]
        while s >= K:
            ans += N-r
            s -= A[l]
            l += 1
        r += 1
    return ans
