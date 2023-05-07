def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Qs = []
    for _ in range(Q):
        L, R, X = map(int, input().split())
        Qs.append((L, R, X))
    return N, A, Q, Qs
