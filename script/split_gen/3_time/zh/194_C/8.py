def solve(N, A):
    ans = 0
    for i in range(1, N):
        for j in range(0, i):
            ans += (A[i] - A[j]) ** 2
    return ans
