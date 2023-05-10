def main():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, end=" ")
    if x * 2 == W and y * 2 == H:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()