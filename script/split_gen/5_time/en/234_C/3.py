def solve(K):
    ans = 0
    for i in range(100):
        ans += 2 * (K % 2) * 10 ** i
        K //= 2
        if K == 0:
            break
    return ans
