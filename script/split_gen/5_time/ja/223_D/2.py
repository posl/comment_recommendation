def solve():
    N, M = map(int, input().split())
    P = list(range(1, N + 1))
    for _ in range(M):
        A, B = map(int, input().split())
        P[A - 1], P[B - 1] = P[B - 1], P[A - 1]
    print(*P)
