Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    for i in range(W):
        cnt = 0
        for j in range(H):
            if C[j][i] == '#':
                cnt += 1
        print(cnt)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    X = [0] * W
    for i in range(W):
        for j in range(H):
            if C[j][i] == '#':
                X[i] += 1
    print(*X)

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    c = [list(input()) for _ in range(h)]
    ans = [0] * w
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[j] += 1
    print(*ans)

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    matrix = []
    for i in range(h):
        matrix.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if matrix[j][i] == "#":
                count += 1
        print(count)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    #print(grid)
    for i in range(H):
        count = 0
        for j in range(W):
            if grid[i][j] == "#":
                count += 1
        print(count, end=" ")
    print()

=======
Suggestion 6

def main():
    # 標準入力の取得
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    # 出力
    for i in range(W):
        count = 0
        for j in range(H):
            if C[j][i] == '#':
                count += 1
        print(count)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    #print(grid)
    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[1][0])
    #print(grid[1][1])
    #print(grid[2][0])
    #print(grid[2][1])
    #print(grid[3][0])
    #print(grid[3][1])
    #print(grid[4][0])
    #print(grid[4][1])
    #print(grid[5][0])
    #print(grid[5][1])
    #print(grid[6][0])
    #print(grid[6][1])
    #print(grid[7][0])
    #print(grid[7][1])

    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[0][2])
    #print(grid[0][3])
    #print(grid[0][4])
    #print(grid[0][5])
    #print(grid[0][6])
    #print(grid[0][7])
    #print(grid[0][8])
    #print(grid[0][9])
    #print(grid[0][10])
    #print(grid[0][11])
    #print(grid[0][12])
    #print(grid[0][13])
    #print(grid[0][14])
    #print(grid[0][15])
    #print(grid[0][16])
    #print(grid[0][17])
    #print(grid[0][18])
    #print(grid[0][19])
    #print(grid[0][20])
    #print(grid[0][21])
    #print(grid[0][22])
    #print(grid[0][23])
    #print(grid[0][24])
    #print(grid[0][25])
    #print(grid[0][26])
    #print(grid[0][27])
    #print(grid[0][28])
    #print(grid[0][29])
    #print(grid[0][30])
    #print(grid[0][31])
    #print(grid[0][32])
    #print(grid[0][33])
    #print(grid[0][34])
    #print(grid[0][35])

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    grid = [list(input()) for _ in range(h)]
    w_lst = [0]*w
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                w_lst[j] += 1
    print(*w_lst)

=======
Suggestion 9

def getNumOfX(H, W, C):
    X = []
    for j in range(W):
        numOfX = 0
        for i in range(H):
            if C[i][j] == "#":
                numOfX += 1
        X.append(numOfX)
    return X

=======
Suggestion 10

def count_x(x, y, c):
    count = 0
    for i in range(len(c)):
        if c[i][y] == '#':
            count += 1
    return count
