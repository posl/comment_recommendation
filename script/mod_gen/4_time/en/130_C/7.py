def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    multi = 0
    if x == W / 2 and y == H / 2:
        multi = 1
    print("{0} {1}".format(area, multi))

if __name__ == '__main__':
    main()