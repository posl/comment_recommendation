Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]

    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if i >> h & 1 or j >> w & 1:
                        continue
                    if C[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for y in range(h):
                for x in range(w):
                    if not i >> y & 1 and not j >> x & 1 and c[y][x] == "#":
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and C[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            tmp = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k & 1) == 0 and (j >> l & 1) == 0:
                        if C[k][l] == '#':
                            tmp += 1
            if tmp == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                if h >> i & 1:
                    continue
                for j in range(W):
                    if w >> j & 1:
                        continue
                    if S[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]

    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and c[i][j] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and grid[h][w] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]

    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 or (w >> j) & 1:
                        continue
                    if c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    H,W,K = map(int,input().split())
    grid = [input() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i & 1) == 0 and (w >> j & 1) == 0 and grid[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    H, W, K = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())
    ans = 0
    for row in range(1 << H):
        for col in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if row >> i & 1 == 0 and col >> j & 1 == 0:
                        if C[i][j] == '#':
                            cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
