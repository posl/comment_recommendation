def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    p = [1, 1]
    visited = [[0] * W for _ in range(H)]
    visited[0][0] = 1
    while True:
        if G[p[0] - 1][p[1] - 1] == 'U':
            if p[0] == 1:
                break
            else:
                p[0] -= 1
        elif G[p[0] - 1][p[1] - 1] == 'D':
            if p[0] == H:
                break
            else:
                p[0] += 1
        elif G[p[0] - 1][p[1] - 1] == 'L':
            if p[1] == 1:
                break
            else:
                p[1] -= 1
        elif G[p[0] - 1][p[1] - 1] == 'R':
            if p[1] == W:
                break
            else:
                p[1] += 1
        if visited[p[0] - 1][p[1] - 1] == 1:
            p = [-1, -1]
            break
        visited[p[0] - 1][p[1] - 1] = 1
    print(*p)

if __name__ == '__main__':
    main()