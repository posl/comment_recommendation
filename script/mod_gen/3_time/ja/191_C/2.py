def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(min(H, W))

if __name__ == '__main__':
    main()