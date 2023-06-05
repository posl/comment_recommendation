def main():
    h,w = map(int,input().split())
    g = [list(input()) for _ in range(h)]
    i,j = 0,0
    while g[i][j] != '.':
        if g[i][j] == 'U':
            if i == 0:
                print(-1)
                return
            i -= 1
        elif g[i][j] == 'D':
            if i == h - 1:
                print(-1)
                return
            i += 1
        elif g[i][j] == 'L':
            if j == 0:
                print(-1)
                return
            j -= 1
        elif g[i][j] == 'R':
            if j == w - 1:
                print(-1)
                return
            j += 1
    print(i+1,j+1)
