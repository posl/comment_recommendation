def solve():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    T = [A[i] + B[i] for i in range(N)]
    T2 = [A[i] * 2 + B[i] for i in range(N)]
    T2.sort()
    T.sort()
    for i in range(N - 1):
        T[i + 1] += T[i]
        T2[i + 1] += T2[i]
    ans = 10 ** 18
    for i in range(N):
        if i >= X:
            ans = min(ans, T[i - X] + (X - 1) * B[i])
        else:
            ans = min(ans, T2[i - X + 1] + (X - i - 1) * B[i])
    print(ans)
solve()
