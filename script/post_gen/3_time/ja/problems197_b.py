Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    x -= 1
    y -= 1
    ans = 1
    for i in range(x+1, h):
        if s[i][y] == ".":
            ans += 1
        else:
            break
    for i in range(x-1, -1, -1):
        if s[i][y] == ".":
            ans += 1
        else:
            break
    for i in range(y+1, w):
        if s[x][i] == ".":
            ans += 1
        else:
            break
    for i in range(y-1, -1, -1):
        if s[x][i] == ".":
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 2

def main():
    h, w, x, y = map(int, input().split())
    s = [list(input()) for i in range(h)]
    x -= 1
    y -= 1
    ans = 1
    for i in range(x + 1, h):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for i in range(x - 1, -1, -1):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for j in range(y + 1, w):
        if s[x][j] == '.':
            ans += 1
        else:
            break
    for j in range(y - 1, -1, -1):
        if s[x][j] == '.':
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 3

def solve():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1

    ans = 0
    for i in range(X, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for j in range(Y, W):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y - 1, -1, -1):
        if S[X][j] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 4

def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for i in range(h)]
    ans = 1
    for i in range(x - 1, -1, -1):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for i in range(x + 1, h):
        if s[i][y] == '.':
            ans += 1
        else:
            break
    for i in range(y - 1, -1, -1):
        if s[x][i] == '.':
            ans += 1
        else:
            break
    for i in range(y + 1, w):
        if s[x][i] == '.':
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 5

def get_input_data():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    return h, w, x, y, s

=======
Suggestion 6

def main():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 1
    for i in range(y-2, -1, -1):
        if s[x-1][i] == "#":
            break
        ans += 1
    for i in range(y, w):
        if s[x-1][i] == "#":
            break
        ans += 1
    for i in range(x-2, -1, -1):
        if s[i][y-1] == "#":
            break
        ans += 1
    for i in range(x, h):
        if s[i][y-1] == "#":
            break
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    #print(H, W, X, Y)
    #print(S)
    #print(S[X])
    #print(S[X][Y])
    count = 0
    if S[X][Y] == ".":
        count += 1
    #print(count)
    for i in range(X-1, -1, -1):
        if S[i][Y] == "#":
            break
        else:
            count += 1
    #print(count)
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        else:
            count += 1
    #print(count)
    for i in range(Y-1, -1, -1):
        if S[X][i] == "#":
            break
        else:
            count += 1
    #print(count)
    for i in range(Y+1, W):
        if S[X][i] == "#":
            break
        else:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    h, w, x, y = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 1
    for i in range(x-1,-1,-1):
        if s[i][y-1] == '#':
            break
        ans += 1
    for i in range(x,h):
        if s[i][y-1] == '#':
            break
        ans += 1
    for i in range(y-1,-1,-1):
        if s[x-1][i] == '#':
            break
        ans += 1
    for i in range(y,w):
        if s[x-1][i] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 9

def check(x,y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if s[x][y] == '#':
        return False
    return True

h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]

ans = 1
x -= 1
y -= 1
for i in range(1,h):
    if check(x-i,y):
        ans += 1
    else:
        break
for i in range(1,w):
    if check(x,y-i):
        ans += 1
    else:
        break
for i in range(1,h):
    if check(x+i,y):
        ans += 1
    else:
        break
for i in range(1,w):
    if check(x,y+i):
        ans += 1
    else:
        break
print(ans)

=======
Suggestion 10

def check(x,y):
    if (x<0) or (x>=h) or (y<0) or (y>=w):
        return False
    if s[x][y] == "#":
        return False
    return True

h,w,x,y=map(int,input().split())
s=[list(input()) for _ in range(h)]
x-=1
y-=1
ans=1
for i in range(x-1,-1,-1):
    if check(i,y):
        ans+=1
    else:
        break
for i in range(x+1,h):
    if check(i,y):
        ans+=1
    else:
        break
for i in range(y-1,-1,-1):
    if check(x,i):
        ans+=1
    else:
        break
for i in range(y+1,w):
    if check(x,i):
        ans+=1
    else:
        break
print(ans)
