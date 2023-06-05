def read_input():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    return H, W, S
