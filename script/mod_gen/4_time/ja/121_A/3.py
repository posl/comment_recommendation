def main():
    h, w = map(int, input().split())
    H, W = map(int, input().split())
    print(h*w - (H*w + W*h - H*W))

if __name__ == '__main__':
    main()