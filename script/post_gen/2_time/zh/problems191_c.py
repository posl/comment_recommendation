Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # H, W = map(int, input().split())
    # S = [input() for _ in range(H)]
    H, W = 5, 5
    S = [
        '.....',
        '.###.',
        '.###.',
        '.###.',
        '.....'
    ]
    # print(H, W, S)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if s[i][j] == '#':
                ans += 1
                s[i][j],s[i][j+1],s[i+1][j],s[i+1][j+1] = '.','.','.','.'
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    #print(S)
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == '#':
                if S[i+1][j] == '#' or S[i][j+1] == '#' or S[i+1][j+1] == '#':
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if s[i][j] == '#':
                if s[i+1][j] == '#' or s[i][j+1] == '#' or s[i+1][j+1] == '#':
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    S = [list(input()) for i in range(H)]
    print(S)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    count = 0
    #print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)
    return

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(1, h-1):
        for j in range(1, w-1):
            if s[i][j] == '#':
                if s[i-1][j] != '#' and s[i][j-1] != '#' and s[i+1][j] != '#' and s[i][j+1] != '#':
                    print(-1)
                    return
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    if ans == 0:
        print(0)
        return

    for i in range(1, H):
        for j in range(1, W):
            if S[i][j] == '#' and S[i - 1][j] == '.' and S[i][j - 1] == '.':
                print(-1)
                return
    print(ans)

=======
Suggestion 9

def main():
    h,w = map(int,input().strip().split())
    s = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                cnt += 1
    print(cnt - 4)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[4][0])
    #print(S[4][1])
    #print(S[5][0])
    #print(S[5][1])
    #print(S[6][0])
    #print(S[6][1])
    #print(S[7][0])
    #print(S[7][1])
    #print(S[8][0])
    #print(S[8][1])
    #print(S[9][0])
    #print(S[9][1])
    #print(S[10][0])
    #print(S[10][1])
    #print(S[11][0])
    #print(S[11][1])
    #print(S[12][0])
    #print(S[12][1])
    #print(S[13][0])
    #print(S[13][1])
    #print(S[14][0])
    #print(S[14][1])
    #print(S[15][0])
    #print(S[15][1])
    #print(S[16][0])
    #print(S[16][1])
    #print(S[17][0])
    #print(S[17][1])
    #print(S[18][0])
    #print(S[18][1])
    #print(S[19][0])
    #print(S[19][1])
    #print(S[20][0])
    #print(S[20][1])
    #print(S[21][0])
    #print(S[21][1])
    #print(S[22][0])
    #print(S[22][1])
    #print(S[23][0])
    #print(S[23][1])
    #print(S[24][0])
    #print(S[24][1])
    #print(S[25][0])
    #print(S[25][1])
