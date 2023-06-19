def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c[i][j] = 1 if c[i][j] == '#' else 0
    for i in range(h):
        for j in range(1, w):
            c[i][j] += c[i][j-1]
    for j in range(w):
        for i in range(1, h):
            c[i][j] += c[i-1][j]
    for i in range(h):
        print(' '.join(map(str, c[i])))
main()
