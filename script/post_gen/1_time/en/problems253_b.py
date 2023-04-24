Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x1, y1 = i, j
            elif S[i][j] == 'o':
                x2, y2 = i, j
    print(max(abs(x1-x2), abs(y1-y2)))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                y1, x1 = i, j
            if S[i][j] == 'o':
                y2, x2 = i, j
    print(max(abs(y1-y2), abs(x1-x2)))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "o":
                x1, y1 = i, j
            elif S[i][j] == "o":
                x2, y2 = i, j
    print(max(abs(x1-x2), abs(y1-y2)))

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                x = i
                y = j
                break
    ans = 0
    for i in range(h):
        ans = max(ans, abs(x - i))
    for j in range(w):
        ans = max(ans, abs(y - j))
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                a = i
                b = j
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                c = i
                d = j
    print(max(abs(a - c), abs(b - d)))

=======
Suggestion 6

def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x1, y1 = i, j
            if s[i][j] == "o":
                x2, y2 = i, j
    print(max(abs(x1-x2), abs(y1-y2)))

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                x1,y1 = i,j
            if s[i][j] == "o":
                x2,y2 = i,j
    print(max(abs(x1-x2),abs(y1-y2)))

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    o1 = o2 = None
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                if o1 is None:
                    o1 = (i, j)
                else:
                    o2 = (i, j)
    print(abs(o1[0] - o2[0]) + abs(o1[1] - o2[1]))

=======
Suggestion 9

def main():
    H,W = input().split()
    H = int(H)
    W = int(W)
    S = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x = i
                y = j
    print(abs(x - (H-1)) + abs(y - (W-1)))
main()

=======
Suggestion 10

def get_input():
    H, W = [int(x) for x in input().split()]
    S = [input() for i in range(H)]
    return H, W, S
