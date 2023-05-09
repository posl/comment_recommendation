Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for j in range(Y+1, W):
        if S[X][j] == '#':
            break
        ans += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == '#':
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
    for i in range(X - 1, -1, -1):
        if S[i][Y] == '#':
            break
        else:
            count += 1
    for i in range(X + 1, H):
        if S[i][Y] == '#':
            break
        else:
            count += 1
    for j in range(Y - 1, -1, -1):
        if S[X][j] == '#':
            break
        else:
            count += 1
    for j in range(Y + 1, W):
        if S[X][j] == '#':
            break
        else:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    X -= 1
    Y -= 1
    ans = 0
    for i in range(Y, W):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    print(ans - 3)

=======
Suggestion 5

def get_input():
    h, w, x, y = map(int, input().split())
    s = [input() for i in range(h)]
    return h, w, x, y, s

=======
Suggestion 6

def main():
    h, w, x, y = map(int, input().split())
    s = [input() for _ in range(h)]
    cnt = 0
    for i in range(x, h):
        if s[i][y-1] == '#':
            break
        cnt += 1
    for i in range(x-2, -1, -1):
        if s[i][y-1] == '#':
            break
        cnt += 1
    for j in range(y, w):
        if s[x-1][j] == '#':
            break
        cnt += 1
    for j in range(y-2, -1, -1):
        if s[x-1][j] == '#':
            break
        cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 1
    for i in reversed(range(Y - 1)):
        if S[X - 1][i] == "#":
            break
        else:
            count += 1
    for i in range(Y, W):
        if S[X - 1][i] == "#":
            break
        else:
            count += 1
    for i in reversed(range(X - 1)):
        if S[i][Y - 1] == "#":
            break
        else:
            count += 1
    for i in range(X, H):
        if S[i][Y - 1] == "#":
            break
        else:
            count += 1
    print(count)

=======
Suggestion 8

def visible_squares():
    H, W, X, Y = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    S[X-1][Y-1] = '0'
    count = 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(X, H):
        if S[i][Y-1] == '#':
            break
        else:
            count += 1
    for i in range(Y-2, -1, -1):
        if S[X-1][i] == '#':
            break
        else:
            count += 1
    for i in range(Y, W):
        if S[X-1][i] == '#':
            break
        else:
            count += 1
    print(count)

=======
Suggestion 9

def visible_squares(h,w,x,y):
    #print(h,w,x,y)
    #print(s)
    #print(s[x-1][y-1])
    count = 0
    for i in range(x-1,-1,-1):
        if s[i][y-1] == '#':
            break
        else:
            count += 1
    #print(count)
    for i in range(x,h):
        if s[i][y-1] == '#':
            break
        else:
            count += 1
    #print(count)
    for j in range(y-1,-1,-1):
        if s[x-1][j] == '#':
            break
        else:
            count += 1
    #print(count)
    for j in range(y,w):
        if s[x-1][j] == '#':
            break
        else:
            count += 1
    #print(count)
    return count

h,w,x,y = map(int,input().split())
s = []
for i in range(h):
    s.append(input())

print(visible_squares(h,w,x,y))

=======
Suggestion 10

def input_to_int_list():
    return list(map(int,input().split()))
