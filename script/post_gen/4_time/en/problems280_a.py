Synthesizing 10/10 solutions (Duplicates hidden)

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
    s = [input() for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    print(count)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]

    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum([1 for i in range(h) for j in range(w) if s[i][j] == '#']))

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    count = 0
    for i in range(h):
        count += s[i].count('#')
    print(count)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    print(sum([s.count('#') for s in [input() for _ in range(h)]]))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum(row.count('#') for row in s))

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(sum(s.count("#") for s in S))
