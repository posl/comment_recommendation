def problems101_c(N, K, A):
    ans = 0
    while N > 0:
        N -= K
        ans += 1
    return ans
