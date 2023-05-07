def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    if W % 2 == 0 and H % 2 == 0 and x == W / 2 and y == H / 2:
        print(area, 1)
    else:
        print(area, 0)

if __name__ == '__main__':
    main()