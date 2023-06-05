def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in ans:
        print(''.join(i))

if __name__ == '__main__':
    main()