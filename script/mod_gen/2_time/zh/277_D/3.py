def solve(N, M, A):
    ans = 0
    A.sort()
    for i in range(N):
        if A[i] <= ans % M:
            ans += M - ans % M + A[i] + 1
        else:
            ans += A[i] - ans % M + 1
    return ans - 1
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))
