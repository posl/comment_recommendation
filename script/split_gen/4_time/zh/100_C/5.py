def solve(N, A):
    # 除以2的次数
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
            ans += 1
    return ans
