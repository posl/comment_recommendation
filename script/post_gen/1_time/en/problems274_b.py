Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for i in range(W):
        for j in range(H):
            if C[j][i] == '#':
                X[i] += 1
    print(*X)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    X = [0] * W
    for i in range(H):
        line = input()
        for j in range(W):
            if line[j] == '#':
                X[j] += 1
    print(*X)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if grid[j][i] == '#':
                ans[i] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for j in range(w):
        print(sum(1 for i in range(h) if a[i][j] == '#'), end=' ')
    print()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    for j in range(W):
        print(sum([1 for i in range(H) if C[i][j] == '#']), end=' ')
    print()
    return

=======
Suggestion 7

def solve():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == '#':
                ans[i] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    X = [0 for i in range(W)]
    for i in range(H):
        S = input()
        for j in range(W):
            if S[j] == '#':
                X[j] += 1
    print(*X)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    for j in range(W):
        print(sum(c[j] == '#' for c in C))

=======
Suggestion 10

def main():
    #read
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    #solve
    ans = [0]*W
    for j in range(W):
        for i in range(H):
            if grid[i][j] == "#":
                ans[j] += 1
    #print
    print(*ans)
