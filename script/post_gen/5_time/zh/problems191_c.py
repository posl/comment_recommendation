Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    ans -= (h + w - 1)
    print(ans)

=======
Suggestion 2

def main():
    print("main")
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(list(input()))
    print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
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
    #print(S[4][0])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[4][4])
    #print(S[5][0])
    #print(S[5][1])
    #print(S[5][2])
    #print(S[5][3])
    #print(S[5][4])
    #print(S[6][0])
    #print(S[6][1])
    #print(S[6][2])
    #print(S[6][3])
    #print(S[6][4])
    #print(S[7][0])
    #print(S[7][1])
    #print(S[7][2])
    #print(S[7][3])
    #print(S[7][4])
    #print(S[8][0])
    #print(S[8][1])
    #print(S[8][2])
    #print(S[8][3])
    #print(S[8][4])
    #print(S[9][0])
    #print(S[9][1])
    #print(S[9][2])
    #print(S[9][3])
    #print(S[9][4])
    #print(S[10][0])
    #print

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    #print(S)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
                if i < H - 1 and S[i + 1][j] == '#':
                    ans -= 1
                if j < W - 1 and S[i][j + 1] == '#':
                    ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    # H,W = map(int, input().split())
    # S = [input() for _ in range(H)]
    H = 5
    W = 5
    S = ['.....', '.###.', '.###.', '.###.', '.....']
    print(H,W,S)
    # x = [i for i in range(H) if S[i].count('#') > 0]
    # y = [i for i in range(W) if ''.join([S[j][i] for j in range(H)]).count('#') > 0]
    # print(x,y)
    # if len(x) < 2 or len(y) < 2:
    #     print(0)
    #     return
    # ans = 0
    # for i in range(len(x) - 1):
    #     for j in range(len(y) - 1):
    #         if S[x[i]][y[j]] == '#' and S[x[i]][y[j + 1]] == '#' and S[x[i + 1]][y[j]] == '#' and S[x[i + 1]][y[j + 1]] == '#':
    #             ans += 1
    # print(ans)
    # return
    x = [i for i in range(H) if S[i].count('#') > 0]
    print(x)
    y = [i for i in range(W) if ''.join([S[j][i] for j in range(H)]).count('#') > 0]
    print(y)
    if len(x) < 2 or len(y) < 2:
        print(0)
        return
    ans = 0
    for i in range(len(x) - 1):
        for j in range(len(y) - 1):
            if S[x[i]][y[j]] == '#' and S[x[i]][y[j + 1]] == '#' and S[x[i + 1]][y[j]] == '#' and S[x[i + 1]][y[j + 1]] == '#':
                ans += 1
    print(ans)
    return

main()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i][j+1] == '#' and S[i+1][j+1] == '#':
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H - 1):
        for j in range(W - 1):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if S[i + k][j + l] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    if ans == H + W - 1:
        print(1)
    elif ans == H + W - 2:
        print(2)
    elif ans == H + W:
        print(4)
    else:
        print(0)

=======
Suggestion 8

def main():
    H,W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == "#":
                if S[i+1][j] == "#" or S[i][j+1] == "#" or S[i+1][j+1] == "#":
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h - 1):
        for j in range(w - 1):
            if s[i][j] == '#':
                if s[i][j + 1] == '#' or s[i + 1][j] == '#' or s[i + 1][j + 1] == '#':
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#':
                if S[i - 1][j] == '.' and S[i + 1][j] == '.' and S[i][j - 1] == '.' and S[i][j + 1] == '.':
                    ans = 1
                    break
    if ans == 0:
        print(0)
    else:
        print(2)
    return 0
