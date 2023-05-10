def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    print(H * W - sum([row.count('#') for row in grid]))

if __name__ == '__main__':
    main()