def get_input():
    N, M = map(int, input().split())
    E = []
    for _ in range(M):
        E.append(tuple(map(int, input().split())))
    return N, M, E
