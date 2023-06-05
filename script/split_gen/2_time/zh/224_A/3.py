def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        A[i] -= 1
        B[i] -= 1
    for i in range(M):
        if ans[A[i]] > ans[B[i]]:
            ans[A[i]], ans[B[i]] = ans[B[i]], ans[A[i]]
    for i in range(N):
        if ans[i] == i + 1:
            print(-1)
            return
    print(*ans)
