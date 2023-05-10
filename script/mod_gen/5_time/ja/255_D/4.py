def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    ans = 0
    for i in range(1, N):
        ans += abs(A[i] - A[i - 1])
    for i in range(Q):
        if i > 0:
            ans -= abs(A[X[i]] - A[X[i] - 1])
        if i < Q - 1:
            ans -= abs(A[X[i + 1]] - A[X[i]])
        ans += abs(A[X[i + 1] - 1] - A[X[i] - 1])
        print(ans)

if __name__ == '__main__':
    solve()