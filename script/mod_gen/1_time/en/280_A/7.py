def main():
    # Read input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # Count the number of squares with pieces
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    # Output the number of squares with pieces
    print(count)

if __name__ == '__main__':
    main()