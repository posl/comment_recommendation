def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(H*W, A*2+B)

if __name__ == '__main__':
    main()