def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M):
        ans[A[i] - 1], ans[B[i] - 1] = ans[B[i] - 1], ans[A[i] - 1]
    print(*ans)

if __name__ == '__main__':
    solve()