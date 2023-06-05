def solve(N, M, A, B):
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if ans[A[i] - 1] > ans[B[i] - 1]:
            ans[A[i] - 1], ans[B[i] - 1] = ans[B[i] - 1], ans[A[i] - 1]
    return ans
