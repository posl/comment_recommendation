def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    i, j = 0, 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if G[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif G[i][j] == 'D':
            if i == H - 1:
                break
            i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif G[i][j] == 'R':
            if j == W - 1:
                break
            j += 1
    print(i + 1, j + 1)
