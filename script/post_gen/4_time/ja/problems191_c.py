Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if s[i+k][j+l] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == "#":
                if S[i - 1][j] == "#" and S[i + 1][j] == "#" and S[i][j - 1] == "#" and S[i][j + 1] == "#":
                    ans += 1
    if ans == 0:
        print(0)
    else:
        print(ans - 1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    if count == 0:
        print(0)
        exit()
    elif count == 1:
        print(1)
        exit()
    else:
        pass
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                start = (i, j)
                break
        else:
            continue
        break
    x, y = start
    next = (x, y+1)
    if next[1] >= W:
        next = (x+1, 0)
    else:
        pass
    count = 1
    while next != start:
        if S[next[0]][next[1]] == "#":
            count += 1
            x, y = next
            next = (x, y+1)
            if next[1] >= W:
                next = (x+1, 0)
            else:
                pass
        else:
            x, y = next
            next = (x, y+1)
            if next[1] >= W:
                next = (x+1, 0)
            else:
                pass
    print(count)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    black = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                black += 1
    if black == H + W - 1:
        print(2)
        return
    if black == H + W - 2:
        print(3)
        return
    if black == H + W - 3:
        print(4)
        return
    print(1)
    return

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1,H-1):
        for j in range(1,W-1):
            if S[i][j] == "#":
                if S[i-1][j] == "." and S[i+1][j] == "." and S[i][j-1] == "." and S[i][j+1] == ".":
                    ans = 1
                    break
        if ans == 1:
            break
    if ans == 1:
        print(2)
    else:
        print(4)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H - 1):
        for j in range(W - 1):
            if S[i][j] == '#':
                cnt += 1
                S[i][j] = '.'
                S[i + 1][j] = '.' 
                S[i][j + 1] = '.' 
                S[i + 1][j + 1] = '.' 
    print(cnt)

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    if ans == h+w-1:
        print(1)
    elif ans == h+w-2:
        print(2)
    else:
        print(4)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    ans -= 4
    ans += H + W - 2
    print(ans)

=======
Suggestion 9

def solve():
    h,w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            cnt = 0
            for x in range(2):
                for y in range(2):
                    if s[i+x][j+y] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 10

def get_input():
    h, w = map(int, input().split())
    return h, w
