def get_input():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    return H, W, a
