def main():
    W, H, x, y = map(int, input().split())
    if W == x * 2 and H == y * 2:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)
