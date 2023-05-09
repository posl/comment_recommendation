def main():
    # Standard Input
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    # Initialize
    count = 1
    # Count up
    # Horizontal
    for i in range(X, H):
        if S[i-1][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        else:
            count += 1
    # Vertical
    for i in range(Y, W):
        if S[X-1][i-1] == '#':
            break
        else:
            count += 1
    for i in range(Y-2, -1, -1):
        if S[X-1][i] == '#':
            break
        else:
            count += 1
    # Standard Output
    print(count)

if __name__ == '__main__':
    main()