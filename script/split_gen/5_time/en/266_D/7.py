def solve():
    N, *T = map(int, open(0).read().split())
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = T[i * 3], T[i * 3 + 1], T[i * 3 + 2]
    ans = 0
    for i in range(N):
        if T[i] <= X[i]:
            ans += A[i]
    print(ans)
