Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in range(w):
        x = 0
        for j in range(h):
            if a[j][i] == "#":
                x += 1
        print(x, end=" ")

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(H):
        X = 0
        for j in range(W):
            if C[i][j] == "#":
                X += 1
        print(X, end=" ")
    print()

=======
Suggestion 3

def count_boxs(grid, W):
    count = 0
    for i in range(W):
        if grid[i] == '#':
            count += 1
    return count

=======
Suggestion 4

def main():
    H,W = map(int,input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    ans = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                ans[j] += 1
    print(*ans)

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(W):
        cnt = 0
        for j in range(H):
            if C[j][i] == '#':
                cnt += 1
        print(cnt)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        C.append(input())
    for i in range(H):
        cnt = 0
        for j in range(W):
            if C[i][j] == '#':
                cnt += 1
        print(cnt)

=======
Suggestion 7

def problems274_b():
    h,w = map(int,input().split())
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        cnt = 0
        for j in range(h):
            if c[j][i] == "#":
                cnt += 1
        print(cnt)

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    for i in range(w):
        cnt = 0
        for j in range(h):
            if c[j][i] == "#":
                cnt += 1
        if cnt == 0:
            continue
        print(cnt, end=" ")
    print("")

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    c = [list(input()) for i in range(h)]
    x = [0] * w
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                x[j] += 1
    for i in range(w):
        print(x[i], end=' ')
    print()

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(h):
        cnt = 0
        for j in range(w):
            if c[i][j] == '#':
                cnt += 1
        print(cnt)
