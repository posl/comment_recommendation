def main():
    H,W = list(map(int, input().split()))
    R,C = list(map(int, input().split()))
    print(H*W - (H+W-1))

if __name__ == '__main__':
    main()