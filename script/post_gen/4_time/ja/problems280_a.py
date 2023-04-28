Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 7

def problems280_a():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1

    print(cnt)

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([si.count('#') for si in s]))
