def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-R) + (W-C) + 1)

if __name__ == '__main__':
    main()