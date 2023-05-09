def solve(N):
    # 1桁目
    ans = 0
    n = 1
    while True:
        if N <= n:
            ans += N
            break
        ans += n
        N -= n
        n *= 2
    # 2桁目以降
    n = 1
    while True:
        if N <= n:
            ans += N * 10
            break
        ans += n * 10
        N -= n
        n *= 2
    return ans
