def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    print(grid)
    print(H, W)

if __name__ == '__main__':
    main()