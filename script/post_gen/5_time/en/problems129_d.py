Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            for k in range(j + 1, w):
                if s[i][k] == '#':
                    break
                t += 1
            for k in range(j - 1, -1, -1):
                if s[i][k] == '#':
                    break
                t += 1
            for k in range(i + 1, h):
                if s[k][j] == '#':
                    break
                t += 1
            for k in range(i - 1, -1, -1):
                if s[k][j] == '#':
                    break
                t += 1
            ans = max(ans, t)
    print(ans + 1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                tmp = 1
                for i in range(h-1, -1, -1):
                    if S[i][w] == '#':
                        break
                    tmp += 1
                for i in range(h+1, H):
                    if S[i][w] == '#':
                        break
                    tmp += 1
                for i in range(w-1, -1, -1):
                    if S[h][i] == '#':
                        break
                    tmp += 1
                for i in range(w+1, W):
                    if S[h][i] == '#':
                        break
                    tmp += 1
                ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def readinput():
    h,w=list(map(int,input().split()))
    s=[]
    for _ in range(h):
        s.append(input())
    return h,w,s

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            cnt = 0
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nh, nw = h+dh, w+dw
                while 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] == '#':
                        break
                    cnt += 1
                    nh += dh
                    nw += dw
            ans = max(ans, cnt)
    print(ans+1)

=======
Suggestion 6

def inputs():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    return h, w, s

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    # print(s)
    w_list = []
    for i in range(h):
        w_list.append(s[i].count('.'))
    # print(w_list)
    h_list = []
    for i in range(w):
        tmp = 0
        for j in range(h):
            if s[j][i] == '.':
                tmp += 1
        h_list.append(tmp)
    # print(h_list)
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                tmp = w_list[i] + h_list[j] - 1
            else:
                tmp = w_list[i] + h_list[j]
            if ans < tmp:
                ans = tmp
    print(ans)

=======
Suggestion 8

def main():
    H, W = [int(x) for x in input().split()]
    S = []
    for i in range(H):
        S.append(input())
    #print(H,W,S)

    # 1. Find the number of squares lighted by the lamp placed at each square
    # 2. Find the maximum number of squares lighted by the lamp

    # 1. Find the number of squares lighted by the lamp placed at each square
    # 1.1. Find the number of squares lighted by the lamp placed at each square in the up direction
    up = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                up[i][j] = 0
            elif i == 0:
                up[i][j] = 1
            else:
                up[i][j] = up[i-1][j] + 1
    #print(up)

    # 1.2. Find the number of squares lighted by the lamp placed at each square in the down direction
    down = [[0 for i in range(W)] for j in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W):
            if S[i][j] == '#':
                down[i][j] = 0
            elif i == H-1:
                down[i][j] = 1
            else:
                down[i][j] = down[i+1][j] + 1
    #print(down)

    # 1.3. Find the number of squares lighted by the lamp placed at each square in the left direction
    left = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                left[i][j] = 0
            elif j == 0:
                left[i][j] = 1
            else:
                left[i][j] = left[i][j-1] + 1
    #print(left)

    # 1.4. Find the number of squares lighted by the lamp placed at each square in the right direction
    right = [[0 for i

=======
Suggestion 9

def lamp(H,W,S):
    #print(H,W,S)
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    #print(S[0][0])
    #print(S[3][5])
    #print(S[0])
    #print(S[3])
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                #print(i,j)
                cnt = 1
                for k in range(j+1,W):
                    if S[i][k] == '#':
                        break
                    else:
                        cnt += 1
                for k in range(j-1,-1,-1):
                    if S[i][k] == '#':
                        break
                    else:
                        cnt += 1
                for k in range(i+1,H):
                    if S[k][j] == '#':
                        break
                    else:
                        cnt += 1
                for k in range(i-1,-1,-1):
                    if S[k][j] == '#':
                        break
