def resolve():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                X[j] += 1
    for i in range(W):
        print(X[i], end=" ")
    print()

if __name__ == '__main__':
    resolve()