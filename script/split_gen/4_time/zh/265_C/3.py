def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    visited = [[False] * W for _ in range(H)]
    while 0 <= i < H and 0 <= j < W:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        elif G[i][j] == 'R':
            j += 1
    print(i + 1, j + 1)
