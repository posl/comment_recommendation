def get_input():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    return N, tlr
