def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))
main()

if __name__ == '__main__':
    main()