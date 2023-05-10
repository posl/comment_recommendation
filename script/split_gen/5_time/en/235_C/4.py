def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        queries.append(tuple(map(int, input().split())))
    return N, Q, A, queries
