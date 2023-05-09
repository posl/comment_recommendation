def get_input_data():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    return H, W, C
