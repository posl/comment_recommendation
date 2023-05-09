def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    i = j = 0
    while True:
        if g[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif g[i][j] == 'D':
            if i == h - 1:
                break
            i += 1
        elif g[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        else:
            if j == w - 1:
                break
            j += 1
    print(i + 1, j + 1)
