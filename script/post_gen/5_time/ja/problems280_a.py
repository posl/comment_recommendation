Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1

    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 3

def main():
    H,W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        ans += S[i].count("#")
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 5

def count_dot(s):
    return s.count('.')

=======
Suggestion 6

def main():
    h,w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    print(sum([s[i].count('#') for i in range(h)]))

=======
Suggestion 8

def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 9

def a():
    h, w = map(int, input().split())
    for i in range(h):
        s = input()
        print(s)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        ans += S[i].count('#')
    print(ans)
