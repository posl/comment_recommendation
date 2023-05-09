def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    print(H * W - sum(row.count('#') for row in grid))

if __name__ == '__main__':
    main()