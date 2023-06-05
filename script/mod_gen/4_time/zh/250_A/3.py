def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - R + 1) * (W - C + 1))

if __name__ == '__main__':
    main()