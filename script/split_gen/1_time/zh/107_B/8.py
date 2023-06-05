def input_data():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    return H, W, a
