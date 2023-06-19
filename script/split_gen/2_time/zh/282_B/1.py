def get_input():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    return N, M, S
