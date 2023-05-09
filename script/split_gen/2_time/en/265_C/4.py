def main():
    h, w = map(int, input().split())
    g = [[c for c in input()] for _ in range(h)]
    i, j = 0, 0
    for _ in range(h*w):
        if g[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif g[i][j] == 'D':
            if i == h-1:
                break
            i += 1
        elif g[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif g[i][j] == 'R':
            if j == w-1:
                break
            j += 1
    else:
        print(-1)
        return
    print(i+1, j+1)
