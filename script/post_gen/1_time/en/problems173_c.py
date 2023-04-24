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
            for k in range(H):
                for l in range(W):
                    if i>>k&1 or j>>l&1:
                        continue
                    if C[k][l] == "#":
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
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if i >> h & 1 == 0 and j >> w & 1 == 0 and C[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
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
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h>>i)&1 == 0 and (w>>j)&1 == 0 and C[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1:
                        continue
                    if (w >> j) & 1:
                        continue
                    if C[i][j] == '#':
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
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i >> k & 1 or j >> l & 1:
                        continue
                    if S[k][l] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                if (h >> i) & 1:
                    continue
                for j in range(W):
                    if (w >> j) & 1:
                        continue
                    if c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]

    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and C[i][j] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    H, W, K = map(int, input().split())
    S = []
    for h in range(H):
        S.append(input())
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h & 1) == 0 and (j >> w & 1) == 0 and S[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 10

def check(c, r, w, h, k):
    count = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#' and (i in r or j in w):
                count += 1
    if count == k:
        return 1
    else:
        return 0

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        row = []
        col = []
        for l in range(h):
            if (i >> l) & 1:
                row.append(l)
        for m in range(w):
            if (j >> m) & 1:
                col.append(m)
        ans += check(c, row, col, h, w, k)
print(ans)

Python3
