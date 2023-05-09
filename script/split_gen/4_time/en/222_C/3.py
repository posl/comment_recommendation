def get_input():
    N, M = map(int, input().split())
    A = []
    for i in range(2 * N):
        A.append(input())
    return N, M, A
