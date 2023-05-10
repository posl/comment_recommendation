def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    flag = 0
    if x == W / 2 and y == H / 2:
        flag = 1
    print(area, flag)

if __name__ == '__main__':
    main()