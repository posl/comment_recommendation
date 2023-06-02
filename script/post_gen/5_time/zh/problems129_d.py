Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    #print(S)
    ans = 0
    for i1 in range(H):
        for j1 in range(W):
            for i2 in range(H):
                for j2 in range(W):
                    if i1 == i2 and j1 == j2:
                        continue
                    if S[i1][j1] == '#' or S[i2][j2] == '#':
                        continue
                    if i1 == i2:
                        ok = True
                        for j in range(min(j1,j2),max(j1,j2)+1):
                            if S[i1][j] == '#':
                                ok = False
                        if ok:
                            ans = max(ans,abs(j1-j2)+1)
                    if j1 == j2:
                        ok = True
                        for i in range(min(i1,i2),max(i1,i2)+1):
                            if S[i][j1] == '#':
                                ok = False
                        if ok:
                            ans = max(ans,abs(i1-i2)+1)

    print(ans)

=======
Suggestion 3

def problems129_d():
    pass

=======
Suggestion 4

def solve():
    # 读取输入
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    # 从左往右，从上往下，分别统计到达每个格子的光线的最远距离
    # 从右往左，从下往上，分别统计到达每个格子的光线的最远距离
    # 然后将两个方向的光线长度求和，即为放置灯照亮的格子数
    # 这里的光线长度是指光线能够到达的最远距离，包括光线发出的格子
    L = [[0] * W for _ in range(H)]
    R = [[0] * W for _ in range(H)]
    U = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue

            if j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i][j - 1] + 1

            if i == 0:
                U[i][j] = 1
            else:
                U[i][j] = U[i - 1][j] + 1

    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if S[i][j] == '#':
                continue

            if j == W - 1:
                R[i][j] = 1
            else:
                R[i][j] = R[i][j + 1] + 1

            if i == H - 1:
                D[i][j] = 1
            else:
                D[i][j] = D[i + 1][j] + 1

    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, L

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            t = 0
            for k in range(i-1,-1,-1):
                if S[k][j] == '#':
                    break
                t += 1
            for k in range(i+1,H):
                if S[k][j] == '#':
                    break
                t += 1
            for k in range(j-1,-1,-1):
                if S[i][k] == '#':
                    break
                t += 1
            for k in range(j+1,W):
                if S[i][k] == '#':
                    break
                t += 1
            ans = max(ans,t)
    print(ans+1)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    print(S)
    for i in range(H):
        for j in range(W):
            print(S[i][j],end='')
        print()
    print(H,W)
    print(S[0][0])
    print(S[0][1])
    print(S[0][2])
    print(S[0][3])
    print(S[0][4])
    print(S[0][5])
    print(S[1][0])
    print(S[1][1])
    print(S[1][2])
    print(S[1][3])
    print(S[1][4])
    print(S[1][5])
    print(S[2][0])
    print(S[2][1])
    print(S[2][2])
    print(S[2][3])
    print(S[2][4])
    print(S[2][5])
    print(S[3][0])
    print(S[3][1])
    print(S[3][2])
    print(S[3][3])
    print(S[3][4])
    print(S[3][5])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    #print(S)
    #print(H, W)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print(S[3][5])
    #print(S[3][6])
    #print(S[3][7])
    #print(S[3][8])
    #print(S[3][9])
    #print(S[3][10])
    #print(S[3][11])
    #print(S[3][12])
    #print(S[3][13])
    #print(S[3][14])
    #print(S[3][15])
    #print(S[3][16])
    #print(S[3][17])
    #print(S[3][18])
    #print(S[3][19])
    #print(S[3][20])
    #print(S[3][21])
    #print(S[3][22])
    #print(S[3][23])
    #print(S[3][24])
    #print(S[3][25])
    #print(S[3][26])
    #print(S[3][27])
    #print(S[3][28])
    #print(S[3][29])
    #print(S[3][30])
    #print(S[3][31])
    #print(S[3][32])
    #print(S[3][33])
    #print(S[3][34])
    #print(S[3][35])
    #print(S[3][36])
    #print(S[3][37])
    #print(S[3][38])
    #print(S[3][39])
    #print(S[3][40
