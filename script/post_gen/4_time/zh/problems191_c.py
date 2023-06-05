Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if s[i][j] == '#':
                if s[i+1][j] == '#' or s[i][j+1] == '#' or s[i+1][j+1] == '#':
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1

    print(count)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            cnt = 0
            for di in range(2):
                for dj in range(2):
                    if s[i+di][j+dj] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == "#" or S[i+1][j] == "#" or S[i][j+1] == "#" or S[i+1][j+1] == "#":
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    s = [list(input()) for i in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1

    return ans

=======
Suggestion 6

def solve(H, W, S):
    # print(H, W, S)
    # print(type(H), type(W), type(S))
    # print(S[0])
    # print(type(S[0]))
    # print(S[0][0])
    # print(type(S[0][0]))
    # print(S[0][0] == '#')
    # print(S[0][0] == '.')
    # print(S[0][1] == '#')
    # print(S[0][1] == '.')
    # print(S[1][0] == '#')
    # print(S[1][0] == '.')
    # print(S[1][1] == '#')
    # print(S[1][1] == '.')

    # print(S[0][0] == '#')
    # print(S[0][0] == '.')
    # print(S[0][1] == '#')
    # print(S[0][1] == '.')

    # print(S[1][0] == '#')
    # print(S[1][0] == '.')
    # print(S[1][1] == '#')
    # print(S[1][1] == '.')

    # print(S[0][0] == '#')
    # print(S[0][0] == '.')
    # print(S[0][1] == '#')
    # print(S[0][1] == '.')
    # print(S[1][0] == '#')
    # print(S[1][0] == '.')
    # print(S[1][1] == '#')
    # print(S[1][1] == '.')

    # print(S[0][0] == '#')
    # print(S[0][0] == '.')
    # print(S[0][1] == '#')
    # print(S[0][1] == '.')
    # print(S[1][0] == '#')
    # print(S[1][0] == '.')
    # print(S[1][1] == '#')
    # print(S[1][1] == '.')

    # print(S[0][0] == '#')
    # print(S[0][0] == '.')
    # print(S[0][1] == '#')
    # print(S[0][1] == '.')
    # print(S[1

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            count = 0
            for di in range(2):
                for dj in range(2):
                    if S[i+di][j+dj] == '#':
                        count += 1
            if count == 1 or count == 3:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    if cnt == 0:
        print(0)
        return
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i == 0 or i == H-1 or j == 0 or j == W-1:
                    ans += 1
                else:
                    if S[i-1][j] == '.' or S[i+1][j] == '.' or S[i][j-1] == '.' or S[i][j+1] == '.':
                        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    res = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "#":
                        res += 1
    print(res//2)
