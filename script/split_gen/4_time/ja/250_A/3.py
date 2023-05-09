def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(H * W - (R - 1) * W - (C - 1) * H + (R - 1) * (C - 1))
