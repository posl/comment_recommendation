def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    maze = [['#'] + m + ['#'] for m in maze]
    maze = [['#' for _ in range(w+2)]] + maze + [['#' for _ in range(w+2)]]
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    visited[ch][cw] = True
    queue = [(ch, cw, 0)]
    while queue:
        x, y, d = queue.pop(0)
        if x == dh and y == dw:
            print(d)
            return
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if maze[i][j] == '.' and not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j, d))
        for i in range(x-2, x+3):
            for j in range(y-2, y+3):
                if maze[i][j] == '.' and not visited[i][j]:
                    visited[i][j] = True
                    queue.append((i, j, d+1))
    print(-1)
main()

if __name__ == '__main__':
    main()