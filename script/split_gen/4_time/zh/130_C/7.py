def main():
    # W, H, x, y = map(int, input().split())
    W, H, x, y = 2, 2, 1, 1
    print(W*H/2, 1 if x*2==W and y*2==H else 0)
    return
