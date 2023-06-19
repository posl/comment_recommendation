def get_input():
    H, W = [int(x) for x in input().split()]
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    return H, W, S, T
