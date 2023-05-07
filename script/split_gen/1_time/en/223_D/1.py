def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [-1] * N
    for i in range(M):
        if ans[A[i] - 1] == -1:
            ans[A[i] - 1] = A[i]
        if ans[B[i] - 1] == -1:
            ans[B[i] - 1] = B[i]
    for i in range(N):
        if ans[i] == -1:
            ans[i] = i + 1
    for i in range(M):
        if ans.index(A[i]) > ans.index(B[i]):
            print(-1)
            return
    print(*ans)
