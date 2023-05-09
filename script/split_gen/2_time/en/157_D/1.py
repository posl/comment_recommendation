def solve():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    ans = [0] * N
    for i in range(M):
        ans[A[i]-1] += 1
        ans[B[i]-1] += 1
    for i in range(K):
        if A[C[i]-1] == D[i]:
            ans[C[i]-1] -= 1
        if B[D[i]-1] == C[i]:
            ans[D[i]-1] -= 1
    for i in range(N):
        ans[i] = N - ans[i] - 1
    print(" ".join(map(str, ans)))
