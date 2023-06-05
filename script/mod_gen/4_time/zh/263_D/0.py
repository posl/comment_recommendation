def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    for i in range(1, N):
        A[i] = min(A[i], A[i - 1] + L)
    for i in range(N - 2, -1, -1):
        A[i] = min(A[i], A[i + 1] + R)
    for i in range(N):
        ans += A[i] - A[i]
    print(ans)

if __name__ == '__main__':
    solve()