Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == '#':
                if S[i+1][j] == '#' or S[i][j+1] == '#' or S[i+1][j+1] == '#':
                    ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                continue
            if i == 0 or i == H-1 or j == 0 or j == W-1:
                ans += 1
                continue
            if S[i-1][j] == '.' or S[i+1][j] == '.' or S[i][j-1] == '.' or S[i][j+1] == '.':
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h,w = map(int, input().split())
    s = [input() for i in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if s[i][j] == '#':
                if s[i+1][j] == '#' or s[i][j+1] == '#' or s[i+1][j+1] == '#':
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1,H-1):
        for j in range(1,W-1):
            if S[i][j] == '#':
                if S[i-1][j] == '.' and S[i+1][j] == '.' and S[i][j-1] == '.' and S[i][j+1] == '.':
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                cnt += 1
    if cnt == 0:
        print(0)
        return
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                if S[i-1][j] == "." or S[i+1][j] == "." or S[i][j-1] == "." or S[i][j+1] == ".":
                    ans += 1
    print(ans)
    return

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    res = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#" and S[i-1][j] == S[i+1][j] == S[i][j-1] == S[i][j+1] == ".":
                res += 1
    print(res)

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    ans -= (H+W-1)
    print(ans)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    #print(count)
    if count == h + w - 1:
        print(1)
    else:
        print(2)

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))

H, W = read_ints()
S = [input() for _ in range(H)]

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    # print(S)

    # print(S[1][2])

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')

    # print(S[1][2] == '#')

    # print(S[1][2] == '.')
