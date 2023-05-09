def solve():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    A = [i + 1 for i in range(N)]
    for i in range(Q):
        A[X[i] - 1], A[X[i]] = A[X[i]], A[X[i] - 1]
    print(*A)

if __name__ == '__main__':
    solve()