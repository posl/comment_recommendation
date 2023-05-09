def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    ans = [0] * N
    for i in range(N):
        ans[i] = i
    for i in range(M):
        if A[i] == 0:
            A[i], B[i] = B[i], A[i]
        else:
            A[i] -= 1
            B[i] -= 1
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        if ans[A[i]] > ans[B[i]]:
            ans[A[i]], ans[B[i]] = ans[B[i]], ans[A[i]]
    for i in range(N):
        if ans[i] == i:
            print(-1)
            return
    print(*[x + 1 for x in ans])

if __name__ == '__main__':
    solve()