def get_input():
    H, W = input().split()
    H = int(H)
    W = int(W)
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    return H, W, S, T
