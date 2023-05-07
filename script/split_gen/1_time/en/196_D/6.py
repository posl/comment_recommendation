def main():
    H, W, A, B = map(int, input().split())
    print((H - B) * (W - A) * A * B)
