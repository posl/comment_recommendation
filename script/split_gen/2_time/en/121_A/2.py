def main():
    # H: number of rows
    # W: number of columns
    # h: number of rows to be painted in black
    # w: number of columns to be painted in black
    H, W, h, w = map(int, input().split())
    print((H - h) * (W - w))
