def read_data():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H, W, S
