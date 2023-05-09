def main():
    W, H, x, y = map(int, input().split())
    ans = W * H / 2
    if x * 2 == W and y * 2 == H:
        print(ans, 1)
    else:
        print(ans, 0)

if __name__ == '__main__':
    main()