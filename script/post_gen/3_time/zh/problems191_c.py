Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)
    return

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    #上下左右
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    #计数器
    cnt = 0

    #遍历
    for i in range(H):
        for j in range(W):
            #如果是黑色
            if S[i][j] == "#":
                #遍历上下左右
                for dx, dy in d:
                    #如果是白色
                    if 0 <= i+dx < H and 0 <= j+dy < W and S[i+dx][j+dy] == ".":
                        #计数器+1
                        cnt += 1
    #输出结果
    print(cnt)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h - 1):
        for j in range(w - 1):
            cnt = 0
            for di in range(2):
                for dj in range(2):
                    if s[i + di][j + dj] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            cnt = 0
            for di, dj in ((0, 0), (0, 1), (1, 0), (1, 1)):
                if S[i+di][j+dj] == '#':
                    cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            cnt = 0
            for di in range(2):
                for dj in range(2):
                    if S[i+di][j+dj] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(1,h-1):
        for j in range(1,w-1):
            if s[i][j] == "#":
                if s[i-1][j] == "." and s[i+1][j] == "." and s[i][j-1] == "." and s[i][j+1] == ".":
                    ans = 1
    if ans == 1:
        print(4)
    else:
        print(2)

=======
Suggestion 10

def main():
    h,w = list(map(int, input().strip().split()))
    s = []
    for i in range(h):
        s.append(input().strip())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)
