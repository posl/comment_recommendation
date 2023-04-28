Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X+1, H):
        if S[i][Y] == '.':
            ans += 1
        else:
            break
    for i in range(X-1, -1, -1):
        if S[i][Y] == '.':
            ans += 1
        else:
            break
    for i in range(Y+1, W):
        if S[X][i] == '.':
            ans += 1
        else:
            break
    for i in range(Y-1, -1, -1):
        if S[X][i] == '.':
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 2

def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    X -= 1
    Y -= 1
    count = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == ".":
            count += 1
        else:
            break
    for i in range(X + 1, H):
        if S[i][Y] == ".":
            count += 1
        else:
            break
    for i in range(Y - 1, -1, -1):
        if S[X][i] == ".":
            count += 1
        else:
            break
    for i in range(Y + 1, W):
        if S[X][i] == ".":
            count += 1
        else:
            break
    print(count)

=======
Suggestion 3

def solve():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, X, Y = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    X -= 1
    Y -= 1

    ans = 0
    for i in range(X, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for j in range(Y, W):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1
    print(ans-3)

main()

=======
Suggestion 5

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1

    ans = 0
    for i in range(x, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1

    for i in range(x+1, h):
        if s[i][y] == '#':
            break
        ans += 1

    for j in range(y, -1, -1):
        if s[x][j] == '#':
            break
        ans += 1

    for j in range(y+1, w):
        if s[x][j] == '#':
            break
        ans += 1

    print(ans - 3)

=======
Suggestion 6

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 1
    for i in range(Y - 2, -1, -1):
        if S[X - 1][i] == '#':
            break
        ans += 1
    for i in range(Y, W):
        if S[X - 1][i] == '#':
            break
        ans += 1
    for i in range(X - 2, -1, -1):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    h, w, x, y = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 1
    for i in range(x, h):
        if s[i][y-1] == '#':
            break
        ans += 1
    for i in range(x-2, -1, -1):
        if s[i][y-1] == '#':
            break
        ans += 1
    for i in range(y, w):
        if s[x-1][i] == '#':
            break
        ans += 1
    for i in range(y-2, -1, -1):
        if s[x-1][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(X-1, -1, -1):
        if S[i][Y-1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y-1] == '#':
            break
        ans += 1
    for i in range(Y-2, -1, -1):
        if S[X-1][i] == '#':
            break
        ans += 1
    for i in range(Y, W):
        if S[X-1][i] == '#':
            break
        ans += 1
    print(ans)

main()

=======
Suggestion 9

def check(x,y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if s[x][y] == '#':
        return False
    return True

=======
Suggestion 10

def problem197_b():
    h,w,x,y = map(int,input().split())
    s = []
    for _ in range(h):
        s.append(input())
    count = 1
    for i in range(1,h):
        if s[x-1][y-1] == '#':
            break
        if x+i <= h and s[x-1+i-1][y-1] == '.':
            count += 1
        else:
            break
    for i in range(1,h):
        if s[x-1][y-1] == '#':
            break
        if x-i >= 1 and s[x-1-i-1][y-1] == '.':
            count += 1
        else:
            break
    for i in range(1,w):
        if s[x-1][y-1] == '#':
            break
        if y+i <= w and s[x-1][y-1+i-1] == '.':
            count += 1
        else:
            break
    for i in range(1,w):
        if s[x-1][y-1] == '#':
            break
        if y-i >= 1 and s[x-1][y-1-i-1] == '.':
            count += 1
        else:
            break
    print(count)
