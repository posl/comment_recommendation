Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())

    ans = 0
    X -= 1
    Y -= 1

    for i in range(X, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1

    for i in range(X + 1, H):
        if S[i][Y] == '#':
            break
        ans += 1

    for j in range(Y, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1

    for j in range(Y + 1, W):
        if S[X][j] == '#':
            break
        ans += 1

    print(ans)

=======
Suggestion 2

def print_grid(grid):
    for line in grid:
        print(line)

=======
Suggestion 3

def judge(s):
    if s == "#":
        return False
    else:
        return True

H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
count = 1
for i in range(X-2, -1, -1):
    if judge(S[i][Y-1]):
        count += 1
    else:
        break
for i in range(X, H):
    if judge(S[i][Y-1]):
        count += 1
    else:
        break
for i in range(Y-2, -1, -1):
    if judge(S[X-1][i]):
        count += 1
    else:
        break
for i in range(Y, W):
    if judge(S[X-1][i]):
        count += 1
    else:
        break
print(count)

=======
Suggestion 4

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    S = [input() for _ in range(h)]
    ans = 1
    for i in range(x+1, h):
        if S[i][y] == '#':
            break
        ans += 1
    for i in range(x-1, -1, -1):
        if S[i][y] == '#':
            break
        ans += 1
    for i in range(y+1, w):
        if S[x][i] == '#':
            break
        ans += 1
    for i in range(y-1, -1, -1):
        if S[x][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 5

def problems197_b():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        ans += 1
    for j in range(Y - 1, -1, -1):
        if S[X - 1][j] == '#':
            break
        ans += 1
    for j in range(Y, W):
        if S[X - 1][j] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h,w,x,y=map(int,input().split())
    s=[input() for _ in range(h)]
    x-=1
    y-=1
    ans=1
    for i in range(x-1,-1,-1):
        if s[i][y]=='#':
            break
        ans+=1
    for i in range(x+1,h):
        if s[i][y]=='#':
            break
        ans+=1
    for i in range(y-1,-1,-1):
        if s[x][i]=='#':
            break
        ans+=1
    for i in range(y+1,w):
        if s[x][i]=='#':
            break
        ans+=1
    print(ans)

=======
Suggestion 7

def problem197_b():
    # 读入数据
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    # 计算答案
    ans = 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y-1] == '#':
            break
        ans += 1
    for j in range(Y-2, -1, -1):
        if S[X-1][j] == '#':
            break
        ans += 1
    for j in range(Y, W):
        if S[X-1][j] == '#':
            break
        ans += 1
    # 输出答案
    print(ans)

=======
Suggestion 8

def main():
    h,w,x,y = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    x -= 1
    y -= 1
    ans = 0
    for i in range(x,-1,-1):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x,h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(y,-1,-1):
        if s[x][i] == '#':
            break
        ans += 1
    for i in range(y,w):
        if s[x][i] == '#':
            break
        ans += 1
    print(ans-3)

=======
Suggestion 9

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
    for j in range(Y-1, -1, -1):
        if S[X][j] == "#":
            break
        ans += 1
    for j in range(Y+1, W):
        if S[X][j] == "#":
            break
        ans += 1

    print(ans)

=======
Suggestion 10

def check(a,b):
    if a < 0 or b < 0 or a >= h or b >= w:
        return False
    if s[a][b] == "#":
        return False
    return True

h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]

ans = 1
for i in range(1,x):
    if not check(x-i-1,y-1):
        break
    ans += 1
for i in range(x,h):
    if not check(i,y-1):
        break
    ans += 1
for i in range(1,y):
    if not check(x-1,y-i-1):
        break
    ans += 1
for i in range(y,w):
    if not check(x-1,i):
        break
    ans += 1
print(ans)
