Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x1, y1 = i, j
            if S[i][j] == 'o':
                x2, y2 = i, j
    print(max(abs(x1-x2), abs(y1-y2)))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x, y = i, j
                break
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                print(abs(x - i) + abs(y - j))
                return

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x, y = i, j
                break
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o" and (i != x or j != y):
                print(abs(x-i)+abs(y-j))
                return

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                a = i
                b = j
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                c = i
                d = j
    print(max(abs(a-c), abs(b-d)))

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x, y = i, j
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                ans = max(ans, abs(x-i)+abs(y-j))
    print(ans)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                a, b = i, j
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                c, d = i, j
    print(max(abs(a-c), abs(b-d)))

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x, y = i, j
    print(max(x, h-x-1) + max(y, w-y-1))

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                x, y = i, j
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                ans = max(ans, abs(x-i) + abs(y-j))
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 二つの駒の位置を求める
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x0, y0 = i, j
            elif S[i][j] == "o":
                x1, y1 = i, j

    # 二つの駒の距離を求める
    ans = abs(x0 - x1) + abs(y0 - y1)

    print(ans)
