def main():
    H,W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    Hs = [0]*H
    Ws = [0]*W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                Hs[i] = 1
                Ws[j] = 1
    for i in range(H):
        if Hs[i] == 1:
            for j in range(W):
                if Ws[j] == 1:
                    print(grid[i][j], end = '')
            print()
