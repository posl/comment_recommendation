Synthesizing 10/10 solutions

=======
Suggestion 1

def check(i, j, S):
    if S[i][j] == '.':
        return False
    if S[i+1][j] == '.':
        return False
    if S[i][j+1] == '.':
        return False
    if S[i+1][j+1] == '.':
        return False
    return True

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                cnt += 1
    if cnt == 0:
        print(0)
        return
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if 0 <= x-1 and S[x-1][y] == "#":
                        stack.append((x-1,y))
                        S[x-1][y] = "."
                    if x+1 < H and S[x+1][y] == "#":
                        stack.append((x+1,y))
                        S[x+1][y] = "."
                    if 0 <= y-1 and S[x][y-1] == "#":
                        stack.append((x,y-1))
                        S[x][y-1] = "."
                    if y+1 < W and S[x][y+1] == "#":
                        stack.append((x,y+1))
                        S[x][y+1] = "."
    print(ans)
    return

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == "#":
                if S[i-1][j] == "." and S[i+1][j] == "." and S[i][j-1] == "." and S[i][j+1] == ".":
                    ans = 1
                    break
        if ans == 1:
            break
    if ans == 1:
        print(4)
    else:
        print(2)

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                cnt += 1
    if cnt == 0:
        print(0)
        exit()
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                if i-1 < 0 or s[i-1][j] == ".":
                    ans += 1
                if j-1 < 0 or s[i][j-1] == ".":
                    ans += 1
                if i+1 >= h or s[i+1][j] == ".":
                    ans += 1
                if j+1 >= w or s[i][j+1] == ".":
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H,W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(1,H-1):
        for j in range(1,W-1):
            if S[i][j] == "#" and S[i-1][j] == "." and S[i+1][j] == "." and S[i][j-1] == "." and S[i][j+1] == ".":
                ans = 1
    if ans == 1:
        print(2)
    else:
        print(4)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        s = input()
        S.append(s)
    #print(S)

    #print(S[0][0])
    #print(S[0][4])
    #print(S[4][0])
    #print(S[4][4])

    #print(S[1][1])
    #print(S[1][3])
    #print(S[3][1])
    #print(S[3][3])

    #print(S[2][2])

    #print(S[1][2])
    #print(S[2][1])
    #print(S[2][3])
    #print(S[3][2])

    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][4])
    #print(S[2][0])
    #print(S[2][4])
    #print(S[3][0])
    #print(S[3][4])
    #print(S[4][1])
    #print(S[4][2])
    #print(S[4][3])

    #print(S[0][2])
    #print(S[2][4])
    #print(S[4][2])
    #print(S[2][0])

    #print(S[0][3])
    #print(S[1][4])
    #print(S[3][4])
    #print(S[4][3])

    #print(S[0][4])
    #print(S[1][3])
    #print(S[3][3])
    #print(S[4][4])

    #print(S[0][0])
    #print(S[1][1])
    #print(S[3][3])
    #print(S[4][4])

    #print(S[0][1])
    #print(S[1][0])
    #print(S[3][4])
    #print(S[4][3])

    #print(S[0][2])
    #print(S[2][0])
    #print(S[4][4])
    #print(S[2][2])

    #print(S[0][3])
    #print(S[3][0])
    #print(S[4][4])
    #print(S[3][3])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and S[i - 1][j] == '.' and S[i][j - 1] == '.' and S[i + 1][j] == '.' and S[i][j + 1] == '.':
                ans += 1
    if ans == 0:
        print(1)
    else:
        print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == '#' and S[i-1][j] == '.' and S[i+1][j] == '.' and S[i][j-1] == '.' and S[i][j+1] == '.':
                ans += 1
    if ans == 0:
        ans = 1
    print(ans)

=======
Suggestion 9

def check(a,b,c,d):
    if a == c and b == d:
        return True
    return False

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    ans = 'Possible' if cnt == H + W - 1 else 'Impossible'
    print(ans)
