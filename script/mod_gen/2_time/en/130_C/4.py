def main():
    W, H, x, y = map(int, input().split())
    ans = W * H / 2
    if x == W / 2 and y == H / 2:
        print(ans, 1)
    else:
        print(ans, 0)

if __name__ == '__main__':
    main()