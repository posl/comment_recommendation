Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_lighted_cells(rows, cols, grid):
    max_lighted_cells = 0
    for row in range(rows):
        for col in range(cols):
            lighted_cells = 0
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, -1, 0)
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, 1, 0)
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, 0, -1)
            lighted_cells += get_lighted_cells_in_direction(row, col, rows, cols, grid, 0, 1)
            if lighted_cells > max_lighted_cells:
                max_lighted_cells = lighted_cells
    return max_lighted_cells

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    # print(H, W)
    # print(S)

    # 1. 先求出每个点的左边、右边、上边、下边的障碍物的个数
    # 2. 再求出每个点的左上、右上、左下、右下的障碍物的个数
    # 3. 最后将每个点的四个方向的障碍物个数相加，再减去左上、右上、左下、右下的障碍物个数，就是该点可以照亮的方格数
    # 4. 求出所有点的照亮方格数的最大值
    # 5. 注意，每个点的左边、右边、上边、下边的障碍物个数，以及左上、右上、左下、右下的障碍物个数，可以用动态规划算出来

    # 1. 先求出每个点的左边、右边、上边、下边的障碍物的个数
    # 2. 再求出每个点的左上、右上、左下、右下的障碍物的个数
    # 3. 最后将每个点的四个方向的障碍物个数相加，再减去左上、右上、左下、右下的障碍物个数，就是该点可以照亮的方格数
    # 4. 求出所有点的照亮方格数的最大值
    # 5. 注意，每个点的左边、右边、上边、下边的障碍物个数，以及左上、右上、左下、右下的障碍物个数，可以用动态规划算出来

    #

=======
Suggestion 3

def get_max_lighting_number():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # print(H, W, S)
    # print(S[0][0])
    # print(S[0][1])
    # print(S[0][2])
    # print(S[0][3])
    # print(S[0][4])
    # print(S[0][5])
    # print(S[0][6])
    # print(S[0][7])
    # print(S[0][8])
    # print(S[0][9])
    # print(S[0][10])
    # print(S[0][11])
    # print(S[1][0])
    # print(S[2][0])
    # print(S[3][0])
    # print(S[4][0])
    # print(S[5][0])
    # print(S[6][0])
    # print(S[7][0])
    # print(S[8][0])
    # print(S[9][0])
    # print(S[10][0])
    # print(S[11][0])
    # print(S[12][0])
    # print(S[13][0])
    # print(S[14][0])
    # print(S[15][0])
    # print(S[16][0])
    # print(S[17][0])
    # print(S[18][0])
    # print(S[19][0])
    # print(S[20][0])
    # print(S[21][0])
    # print(S[22][0])
    # print(S[23][0])
    # print(S[24][0])
    # print(S[25][0])
    # print(S[26][0])
    # print(S[27][0])
    # print(S[28][0])
    # print(S[29][0])
    # print(S[30][0])
    # print(S[31][0])
    # print(S[32][0])
    # print(S[33][0])
    # print(S[34][0])
    # print(S[35][0])
    # print(S[36][0])
    # print(S[37][0])
    # print(S[38][0])
    # print(S[39][0])
    #

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def get_max_light(H,W,S):
    #S = [list(s) for s in S]
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[0][7])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[1][5])
    #print(S[1][6])
    #print(S[1][7])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[2][5])
    #print(S[2][6])
    #print(S[2][7])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print(S[3][5])
    #print(S[3][6])
    #print(S[3][7])
    #print(S[4][0])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[4][4])
    #print(S[4][5])
    #print(S[4][6])
    #print(S[4][7])
    #print(S[5][0])
    #print(S[5][1])
    #print(S[5][2])
    #print(S[5][3])
    #print(S[5][4])
    #print(S[5][5])
    #print(S[5][6])
    #print(S[5][7])
    #print(S[6][0])
    #print(S[6][1])
    #print(S[6][2])
    #print(S[6][3])
    #print(S[6][

=======
Suggestion 7

def get_max_lighting_num(h, w, s):
    #print("h: {}, w: {}, s: {}".format(h, w, s))
    max_lighting_num = 0
    for i in range(h):
        lighting_num = 0
        for j in range(w):
            if s[i][j] == '#':
                lighting_num = 0
            else:
                lighting_num += 1
                max_lighting_num = max(max_lighting_num, lighting_num)
        #print("lighting_num: {}".format(lighting_num))
    #print("max_lighting_num: {}".format(max_lighting_num))

    for j in range(w):
        lighting_num = 0
        for i in range(h):
            if s[i][j] == '#':
                lighting_num = 0
            else:
                lighting_num += 1
                max_lighting_num = max(max_lighting_num, lighting_num)
        #print("lighting_num: {}".format(lighting_num))
    #print("max_lighting_num: {}".format(max_lighting_num))

    return max_lighting_num - 1

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    #print(S)
    #print(len(S[0]))
    #print(len(S))
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[0][7])
    #print(S[0][8])
    #print(S[0][9])
    #print(S[0][10])
    #print(S[0][11])
    #print(S[0][12])
    #print(S[0][13])
    #print(S[0][14])
    #print(S[0][15])
    #print(S[0][16])
    #print(S[0][17])
    #print(S[0][18])
    #print(S[0][19])
    #print(S[0][20])
    #print(S[0][21])
    #print(S[0][22])
    #print(S[0][23])
    #print(S[0][24])
    #print(S[0][25])
    #print(S[0][26])
    #print(S[0][27])
    #print(S[0][28])
    #print(S[0][29])
    #print(S[0][30])
    #print(S[0][31])
    #print(S[0][32])
    #print(S[0][33])
    #print(S[0][34])
    #print(S[0][35])
    #print(S[0][36])
    #print(S[0][37])
    #print(S[0][38])
    #print(S[0][39])
    #print(S[0][40])
    #print(S[0][41])
    #print(S[0][42])
    #print(S[0][43])
    #print(S[0][44])
    #print(S[0][45])
    #print(S[0][46])
    #print(S[0][47])
    #print(S[0][48])
    #print(S[0][49])

=======
Suggestion 9

def main():
    print('hello world!')

=======
Suggestion 10

def get_input():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H, W, S
