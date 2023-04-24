Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            ans = max(ans, bfs(i, j, S))
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            cnt = 0
            for k in range(j+1, W):
                if S[i][k] == '#':
                    break
                cnt += 1
            for k in range(j-1, -1, -1):
                if S[i][k] == '#':
                    break
                cnt += 1
            for k in range(i+1, H):
                if S[k][j] == '#':
                    break
                cnt += 1
            for k in range(i-1, -1, -1):
                if S[k][j] == '#':
                    break
                cnt += 1
            ans = max(ans, cnt)
    print(ans+1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(4):
                cnt = 1
                while True:
                    if k == 0:
                        if i - cnt < 0 or S[i - cnt][j] == '#':
                            break
                        cnt += 1
                    elif k == 1:
                        if i + cnt > H - 1 or S[i + cnt][j] == '#':
                            break
                        cnt += 1
                    elif k == 2:
                        if j - cnt < 0 or S[i][j - cnt] == '#':
                            break
                        cnt += 1
                    elif k == 3:
                        if j + cnt > W - 1 or S[i][j + cnt] == '#':
                            break
                        cnt += 1
                ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            cnt = 0
            for x in range(i, h):
                if s[x][j] == "#":
                    break
                cnt += 1
            for x in range(i, -1, -1):
                if s[x][j] == "#":
                    break
                cnt += 1
            for y in range(j, w):
                if s[i][y] == "#":
                    break
                cnt += 1
            for y in range(j, -1, -1):
                if s[i][y] == "#":
                    break
                cnt += 1
            ans = max(ans, cnt - 3)
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            cnt = 0
            for k in range(i, -1, -1):
                if S[k][j] == '#':
                    break
                cnt += 1
            for k in range(i, H):
                if S[k][j] == '#':
                    break
                cnt += 1
            for k in range(j, -1, -1):
                if S[i][k] == '#':
                    break
                cnt += 1
            for k in range(j, W):
                if S[i][k] == '#':
                    break
                cnt += 1
            ans = max(ans, cnt)
    print(ans - 3)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue

            # 上下左右の候補を作成
            cand = [(h, w)]
            for i in range(1, max(H, W)):
                if h - i >= 0:
                    cand.append((h - i, w))
                if h + i < H:
                    cand.append((h + i, w))
                if w - i >= 0:
                    cand.append((h, w - i))
                if w + i < W:
                    cand.append((h, w + i))

            # 候補の中から、#があるものを除外
            cand = list(filter(lambda x: S[x[0]][x[1]] != '#', cand))

            # 候補が多い方を採用
            if len(cand) > ans:
                ans = len(cand)

    print(ans)

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                cnt = 0
                ni,nj = i,j
                while 0<=ni<h and 0<=nj<w:
                    if s[ni][nj] == "#":
                        break
                    cnt += 1
                    ni += di
                    nj += dj
                ans = max(ans,cnt)
    print(ans)
main()

I'm not sure if this is the best way to do it, but it's the way I thought of. You can just check all the squares and see if you can light them up, and then you just take the max of all the squares you can light up. I think this is a O(n^3) solution, but I'm not sure.

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    count = [[0] * W for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            for x in range(w + 1, W):
                if S[h][x] == '#':
                    break
                count[h][x] += 1
            for x in range(w - 1, -1, -1):
                if S[h][x] == '#':
                    break
                count[h][x] += 1
            for y in range(h + 1, H):
                if S[y][w] == '#':
                    break
                count[y][w] += 1
            for y in range(h - 1, -1, -1):
                if S[y][w] == '#':
                    break
                count[y][w] += 1
    for h in range(H):
        for w in range(W):
            ans = max(ans, count[h][w])
    print(ans + 1)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)
    
    # up
    up = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0:
                if S[i][j] == '.':
                    up[i][j] = 1
                else:
                    up[i][j] = 0
            else:
                if S[i][j] == '.':
                    up[i][j] = up[i-1][j] + 1
                else:
                    up[i][j] = 0
    #print(up)
    
    # down
    down = [[0] * W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W):
            if i == H-1:
                if S[i][j] == '.':
                    down[i][j] = 1
                else:
                    down[i][j] = 0
            else:
                if S[i][j] == '.':
                    down[i][j] = down[i+1][j] + 1
                else:
                    down[i][j] = 0
    #print(down)
    
    # left
    left = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if j == 0:
                if S[i][j] == '.':
                    left[i][j] = 1
                else:
                    left[i][j] = 0
            else:
                if S[i][j] == '.':
                    left[i][j] = left[i][j-1] + 1
                else:
                    left[i][j] = 0
    #print(left)
    
    # right
    right = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W-1, -1, -1):
            if j == W-1:
                if S[i][j] == '.':
                    right[i][j] = 1
                else:
                    right[i][j] = 0
            else:
                if

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(S)
    #print(H, W)
    #print(S)
    #print(S[0])
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[1][5])
    #print(S[1][6])
    #print(S[2])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[2][5])
    #print(S[2][6])
    #print(S[3])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print(S[3][5])
    #print(S[3][6])
    #print(S[4])
    #print(S[4][0])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])
    #print(S[4][4])
    #print(S[4][5])
    #print(S[4][6])
    #print(S[5])
    #print(S[5][0])
    #print(S[5][1])
    #print(S[5][2])
    #print(S[5][3])
    #print(S[5][4])
    #print(S[5][5])
    #print(S[5][6])
    #print(S[6])
    #print(S[6][0])
    #print(S[6][1])
    #print(S[6][2])
    #print
