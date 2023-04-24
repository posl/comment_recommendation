Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and C[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and C[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if ((i >> k) & 1) == 0 and ((j >> l) & 1) == 0 and S[k][l] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for a in range(h):
                for b in range(w):
                    if c[a][b] == '#' and i >> a & 1 == 0 and j >> b & 1 == 0:
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i >> k & 1 == 0 and j >> l & 1 == 0 and grid[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i>>k & 1) or (j>>l & 1):
                        continue
                    if S[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H,W,K = map(int,input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if i>>h&1 == 0 and j>>w&1 == 0 and C[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    h, w, k = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for r in range(h):
                for c in range(w):
                    if i >> r & 1 or j >> c & 1:
                        continue
                    if grid[r][c] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

main()

=======
Suggestion 9

def solve():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and grid[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 10

def  main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
