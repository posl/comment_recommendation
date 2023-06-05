def get_input():
    H, W = input().split()
    H = int(H)
    W = int(W)
    S = []
    for i in range(H):
        S.append(input())
    return H, W, S
