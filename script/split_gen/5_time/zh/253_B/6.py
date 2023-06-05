def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    return H, W, S
