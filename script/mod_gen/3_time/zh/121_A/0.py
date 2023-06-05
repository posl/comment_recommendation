def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H*W - h*W - H*w + h*w)

if __name__ == '__main__':
    main()