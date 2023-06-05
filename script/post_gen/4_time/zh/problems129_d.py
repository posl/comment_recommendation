Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                cnt = 1
                for k in range(i - 1, -1, -1):
                    if S[k][j] == '#':
                        break
                    cnt += 1
                for k in range(i + 1, H):
                    if S[k][j] == '#':
                        break
                    cnt += 1
                for k in range(j - 1, -1, -1):
                    if S[i][k] == '#':
                        break
                    cnt += 1
                for k in range(j + 1, W):
                    if S[i][k] == '#':
                        break
                    cnt += 1
                ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def get_max_light_num(h,w,grid):
    light_num = 0
    for i in range(1,h+1):
        for j in range(1,w+1):
            if grid[i][j] == '#':
                continue
            else:
                light_num = max(light_num, get_light_num(i,j,h,w,grid))
    return light_num

=======
Suggestion 3

def problem129_d():
    pass

=======
Suggestion 4

def light_num(h, w, s):
    # 从左往右，从上往下
    # 左右方向
    left = [[0] * w for i in range(h)]
    right = [[0] * w for i in range(h)]
    # 上下方向
    up = [[0] * w for i in range(h)]
    down = [[0] * w for i in range(h)]
    # 左右方向
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                left[i][j] = 0
            elif j == 0:
                left[i][j] = 1
            else:
                left[i][j] = left[i][j-1] + 1
    for i in range(h):
        for j in range(w-1, -1, -1):
            if s[i][j] == '#':
                right[i][j] = 0
            elif j == w-1:
                right[i][j] = 1
            else:
                right[i][j] = right[i][j+1] + 1
    # 上下方向
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                up[i][j] = 0
            elif i == 0:
                up[i][j] = 1
            else:
                up[i][j] = up[i-1][j] + 1
    for i in range(h-1, -1, -1):
        for j in range(w):
            if s[i][j] == '#':
                down[i][j] = 0
            elif i == h-1:
                down[i][j] = 1
            else:
                down[i][j] = down[i+1][j] + 1
    # 计算最大值
    max_num = 0
    for i in range(h):
        for j in range(w):
            max_num = max(max_num, left[i][j]+right[i][j]+up[i][j]+down[i][j]-3)
    return max_num

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    #print(H,W,S)
    #print(S[0][1])
    #print(S[1][2])
    #print(S[2][3])
    #print(S[3][4])
    #print(S[4][5])
    #print(S[5][6])
    #print(S[6][7])
    #print(S[7][8])
    #print(S[8][9])
    #print(S[9][10])
    #print(S[10][11])
    #print(S[11][12])
    #print(S[12][13])
    #print(S[13][14])
    #print(S[14][15])
    #print(S[15][16])
    #print(S[16][17])
    #print(S[17][18])
    #print(S[18][19])
    #print(S[19][20])
    #print(S[20][21])
    #print(S[21][22])
    #print(S[22][23])
    #print(S[23][24])
    #print(S[24][25])
    #print(S[25][26])
    #print(S[26][27])
    #print(S[27][28])
    #print(S[28][29])
    #print(S[29][30])
    #print(S[30][31])
    #print(S[31][32])
    #print(S[32][33])
    #print(S[33][34])
    #print(S[34][35])
    #print(S[35][36])
    #print(S[36][37])
    #print(S[37][38])
    #print(S[38][39])
    #print(S[39][40])
    #print(S[40][41])
    #print(S[41][42])
    #print(S[42][43])
    #print(S[43][44])
    #print(S[44][45])
    #print(S[45][46])
    #print(S[46][47])
    #print(S[47][48])
    #print(S[48][49])
    #print(S[49][50])
    #print(S[50][51])
    #print(S[51][52])

=======
Suggestion 6

def light_num(h,w,s):
    #h,w,s = list(map(int,s.split()))
    #s = list(map(int,s.split()))
    #s = [input() for i in range(h)]
    #print(s)
    #print(s[0][0])
    #print(s[1][0])
    #print(s[2][0])
    #print(s[3][0])
    #print(s[4][0])
    #print(s[5][0])
    #print(s[6][0])
    #print(s[7][0])
    #print(s[0][1])
    #print(s[1][1])
    #print(s[2][1])
    #print(s[3][1])
    #print(s[4][1])
    #print(s[5][1])
    #print(s[6][1])
    #print(s[7][1])
    #print(s[0][2])
    #print(s[1][2])
    #print(s[2][2])
    #print(s[3][2])
    #print(s[4][2])
    #print(s[5][2])
    #print(s[6][2])
    #print(s[7][2])
    #print(s[0][3])
    #print(s[1][3])
    #print(s[2][3])
    #print(s[3][3])
    #print(s[4][3])
    #print(s[5][3])
    #print(s[6][3])
    #print(s[7][3])
    #print(s[0][4])
    #print(s[1][4])
    #print(s[2][4])
    #print(s[3][4])
    #print(s[4][4])
    #print(s[5][4])
    #print(s[6][4])
    #print(s[7][4])
    #print(s[0][5])
    #print(s[1][5])
    #print(s[2][5])
    #print(s[3][5])
    #print(s[4][5])
    #print(s[5][5])
    #print(s[6][5])
    #print(s[7][5])
    #print(s[0][6])
    #print(s[1][6])
    #print(s

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            for k in range(j-1,-1,-1):
                if s[i][k] == '#':
                    break
                t += 1
            for k in range(j+1,w):
                if s[i][k] == '#':
                    break
                t += 1
            for k in range(i-1,-1,-1):
                if s[k][j] == '#':
                    break
                t += 1
            for k in range(i+1,h):
                if s[k][j] == '#':
                    break
                t += 1
            ans = max(ans,t)
    print(ans+1)

=======
Suggestion 8

def get_squares(row,col):
    squares = 0
    for i in range(row):
        if i == 0 or i == row - 1:
            squares += col
        else:
            squares += 2
    return squares

=======
Suggestion 9

def get_max_lighted_square_area(grid):
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                continue
            area = 1
            for k in range(i-1, -1, -1):
                if grid[k][j] == '#':
                    break
                area += 1
            for k in range(i+1, len(grid)):
                if grid[k][j] == '#':
                    break
                area += 1
            for k in range(j-1, -1, -1):
                if grid[i][k] == '#':
                    break
                area += 1
            for k in range(j+1, len(grid[0])):
                if grid[i][k] == '#':
                    break
                area += 1
            if area > max_area:
                max_area = area
    return max_area

=======
Suggestion 10

def get_max_light_count(h, w, grid):
    # 从上往下第i行和从左往下第j列的方格上有一个障碍物
    # 从上往下第i行和从左往下第j列的方格上没有一个障碍物
    # 从上往下第i行和从左往下第j列的方格上有一个灯
    # 从上往下第i行和从左往下第j列的方格上没有一个灯
    # 从上往下第i行和从左往下第j列的方格上有一个障碍物并且有一个灯
    # 从上往下第i行和从左往下第j列的方格上有一个障碍物并且没有一个灯
    # 从上往下第i行和从左往下第j列的方格上没有一个障碍物并且有一个灯
    # 从上往下第i行和从左往下第j列的方格上没有一个障碍物并且没有一个灯
    # 从上往下第i行和从左往下第j列的方格上有一个障碍物并且有一个灯
    # 从上往下第i行和从左往下第j列的方格上有一个障碍物并且没有一个灯
    # 从上往下第i行和从左往下第j列的方格上没有一个障碍物并且有一个灯
    # 从上往下第i行和从左往下第j列的方格上没有一个障碍物并且没有一个灯
    # 从上往下第i行和从左往下第j列的方格上有一个障碍物并且有一个灯
    # 从上往下第i行和从左往下
