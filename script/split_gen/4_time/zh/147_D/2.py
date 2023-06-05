def xor_sum(n, a):
    ans = 0
    for i in range(n):
        ans ^= a[i]
    return ans
