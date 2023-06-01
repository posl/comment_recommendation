Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1

    if count == 0:
        return 0
    else:
        return 1

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans - (H + W - 1))
solve()

=======
Suggestion 3

def solve():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#':
                if S[i - 1][j] == '.':
                    ans += 1
                if S[i + 1][j] == '.':
                    ans += 1
                if S[i][j - 1] == '.':
                    ans += 1
                if S[i][j + 1] == '.':
                    ans += 1
    if ans == 0:
        print(0)
    else:
        print(ans // 2 + 1)

=======
Suggestion 4

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
Suggestion 5

def main():
    h,w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 6

def problems191_c():
    pass

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    if ans == 0:
        print(0)
        return
    ans += 4
    ans -= 2 * (H + W)
    print(ans)

=======
Suggestion 8

def main():
    # H, W = map(int, input().split())
    H, W = 5, 5
    # S = [input() for _ in range(H)]
    S = ['.....', '.###.', '.###.', '.###.', '.....']
    # S = ['.....', '.###.', '.###.', '.###.', '.....']
    print(S)
    print(H, W)
    print(S[0][0])
    print(S[0][1])
    print(S[0][2])
    print(S[0][3])
    print(S[0][4])
    print(S[1][0])
    print(S[1][1])
    print(S[1][2])
    print(S[1][3])
    print(S[1][4])
    print(S[2][0])
    print(S[2][1])
    print(S[2][2])
    print(S[2][3])
    print(S[2][4])
    print(S[3][0])
    print(S[3][1])
    print(S[3][2])
    print(S[3][3])
    print(S[3][4])
    print(S[4][0])
    print(S[4][1])
    print(S[4][2])
    print(S[4][3])
    print(S[4][4])

    # print(S[0][0], S[0][1], S[0][2], S[0][3], S[0][4])
    # print(S[1][0], S[1][1], S[1][2], S[1][3], S[1][4])
    # print(S[2][0], S[2][1], S[2][2], S[2][3], S[2][4])
    # print(S[3][0], S[3][1], S[3][2], S[3][3], S[3][4])
    # print(S[4][0], S[4][1], S[4][2], S[4][3], S[4][4])

    # print(S)
    # print(S[0][0], S[0][1], S[0][2], S[0][3], S[0][4])
    # print(S[1][0], S[

=======
Suggestion 9

def main():
    h,w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans-4)

=======
Suggestion 10

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
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and S[i - 1][j] == '.' and S[i + 1][j] == '.' and S[i][j - 1] == '.' and S[i][j + 1] == '.':
                ans += 1
    if ans == 0:
        print(1)
        return
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and ((S[i - 1][j] == '.' and S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i][j + 1] == '.') or (S[i - 1][j] == '#' and S[i + 1][j] == '.' and S[i][j - 1] == '.' and S[i][j + 1] == '#') or (S[i - 1][j] == '#' and S[i + 1][j] == '#' and S[i][j - 1] == '.' and S[i][j + 1] == '.') or (S[i - 1][j] == '.' and S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i][j + 1] == '#')):
                ans += 1
    if ans == 0:
        print(2)
        return
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and ((S[i - 1][j] == '.' and S[i + 1][j] == '.' and S[i][j - 1
