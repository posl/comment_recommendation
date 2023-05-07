def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(4 - (H == 1) - (W == 1) - (R == H) - (C == W))
main()

if __name__ == '__main__':
    main()