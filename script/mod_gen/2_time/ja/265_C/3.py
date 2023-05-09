def main():
    h, w = map(int, input().split())
    g = [list(input()) for i in range(h)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    for k in range(1000000):
        if i == h-1 and j == w-1:
            print(i+1, j+1)
            return
        if g[i][j] == 'U':
            i += di[0]
            j += dj[0]
        elif g[i][j] == 'D':
            i += di[1]
            j += dj[1]
        elif g[i][j] == 'L':
            i += di[2]
            j += dj[2]
        elif g[i][j] == 'R':
            i += di[3]
            j += dj[3]
    print(-1)

if __name__ == '__main__':
    main()