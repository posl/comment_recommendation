def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    i, j = 0, 0
    while 1:
        g[i] = g[i][:j] + 'x' + g[i][j+1:]
        if g[i][j] == 'x':
            print(-1)
            break
        elif g[i][j] == 'U':
            i -= 1
        elif g[i][j] == 'D':
            i += 1
        elif g[i][j] == 'L':
            j -= 1
        elif g[i][j] == 'R':
            j += 1
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i+1, j+1)
            break
main()
