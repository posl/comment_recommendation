Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == "#":
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for _ in range(h)]
    ans = 1
    for i in range(x - 1, -1, -1):
        if s[i][y] == "#":
            break
        ans += 1
    for i in range(x + 1, h):
        if s[i][y] == "#":
            break
        ans += 1
    for j in range(y - 1, -1, -1):
        if s[x][j] == "#":
            break
        ans += 1
    for j in range(y + 1, w):
        if s[x][j] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    X -= 1
    Y -= 1
    count = 1
    for i in range(X + 1, H):
        if S[i][Y] == ".":
            count += 1
        else:
            break
    for i in range(X - 1, -1, -1):
        if S[i][Y] == ".":
            count += 1
        else:
            break
    for i in range(Y + 1, W):
        if S[X][i] == ".":
            count += 1
        else:
            break
    for i in range(Y - 1, -1, -1):
        if S[X][i] == ".":
            count += 1
        else:
            break
    print(count)

=======
Suggestion 4

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1
    ans = 0
    for i in range(x, h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x, -1, -1):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(y, w):
        if s[x][i] == '#':
            break
        ans += 1
    for i in range(y, -1, -1):
        if s[x][i] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 5

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(X - 1, -1, -1):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    for i in range(Y - 1, -1, -1):
        if S[X - 1][i] == '#':
            break
        ans += 1
    for i in range(Y, W):
        if S[X - 1][i] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 6

def solve():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
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
    for j in range(Y-1, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y+1, W):
        if S[X][j] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 1
    for i in range(1, H):
        if S[X-1-i][Y-1] == "#":
            break
        count += 1
    for i in range(1, H):
        if S[X-1+i][Y-1] == "#":
            break
        count += 1
    for i in range(1, W):
        if S[X-1][Y-1-i] == "#":
            break
        count += 1
    for i in range(1, W):
        if S[X-1][Y-1+i] == "#":
            break
        count += 1
    print(count)

=======
Suggestion 8

def main():
    #入力
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]

    #マス (x, y) から見えるマスの数を数える
    ans = 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        i, j = x - 1, y - 1
        while True:
            i += dx
            j += dy
            if not (0 <= i < h and 0 <= j < w):
                break
            if s[i][j] == '#':
                break
            ans += 1

    #出力
    print(ans)

=======
Suggestion 9

def main():
    H,W,X,Y = map(int,input().split())
    S = [input() for i in range(H)]
    count = 0
    for i in range(X-1):
        if S[X-2-i][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(H-X):
        if S[X+i][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(Y-1):
        if S[X-1][Y-2-i] == '#':
            break
        else:
            count += 1
    for i in range(W-Y):
        if S[X-1][Y+i] == '#':
            break
        else:
            count += 1
    print(count+1)

=======
Suggestion 10

def main():
    H,W,X,Y = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    #print(S)
    #print(H,W,X,Y)
    #print(S[X-1][Y-1])
    if S[X-1][Y-1] == '#':
        print('0')
        return
    #print(S[X-1][Y-1])
    count = 1
    #print('count=',count)
    for i in range(1,100):
        if Y-1-i >= 0 and S[X-1][Y-1-i] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    for i in range(1,100):
        if Y-1+i < W and S[X-1][Y-1+i] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    for i in range(1,100):
        if X-1-i >= 0 and S[X-1-i][Y-1] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    for i in range(1,100):
        if X-1+i < H and S[X-1+i][Y-1] == '.':
            count += 1
            #print('count=',count)
        else:
            break
    #print('count=',count)
    print(count)
    return
