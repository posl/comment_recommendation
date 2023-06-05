def get_input():
    N, M = map(int, input().split())
    A = [list(input()) for i in range(2*N)]
    return N, M, A
