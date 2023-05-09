Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        print(count)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    c = []
    for i in range(H):
        c.append(input())
    for i in range(W):
        count = 0
        for j in range(H):
            if c[j][i] == '#':
                count += 1
        print(count)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in range(w):
        cnt = 0
        for j in range(h):
            if a[j][i] == '#':
                cnt += 1
        print(cnt)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    for i in range(w):
        print(sum([1 for j in range(h) if c[j][i] == '#']))

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    ans = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                ans[j] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(w):
        print(sum(c[j][i] == '#' for j in range(h)))

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    res = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                res[j] += 1
    print(*res)

=======
Suggestion 8

def main():
    line = input()
    H, W = line.split()
    H = int(H)
    W = int(W)
    C = []
    for i in range(H):
        line = input()
        C.append(line)
    for j in range(W):
        X_j = 0
        for i in range(H):
            if C[i][j] == "#":
                X_j += 1
        print(X_j, end=" ")
    print()

main()

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    for i in range(h):
        print(input().count('#'))

=======
Suggestion 10

def print_grid(grid):
    for row in grid:
        print(row)
