def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    i, j = 0, 0
    while True:
        if i < 0 or i >= H or j < 0 or j >= W:
            print(-1)
            return
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
main()
