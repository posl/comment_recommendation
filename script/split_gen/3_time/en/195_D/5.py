def solve():
    N, M, Q = map(int, input().split())
    W = [0] + list(map(int, input().split()))
    V = [0] + list(map(int, input().split()))
    X = [0] + list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        A = [0] + [1] * M
        for i in range(L, R+1):
            A[i] = 0
        ans = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if A[j] == 1 and X[j] >= W[i]:
                    ans += V[i]
                    A[j] = 0
                    break
        print(ans)
solve()
