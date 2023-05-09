def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    if W / 2 == x and H / 2 == y:
        print(area, 1)
    else:
        print(area, 0)
