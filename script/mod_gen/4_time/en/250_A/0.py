def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - 1) * (W - 1) - (H - R) * (W - C))
    return

if __name__ == '__main__':
    main()