Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if ((i >> k) & 1) == 0 and ((j >> l) & 1) == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                if (i >> k) & 1:
                    continue
                for l in range(W):
                    if (j >> l) & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 and (w >> j) & 1 and c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if ((i >> k) & 1) == 0 and ((j >> l) & 1) == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for i in range(h)]
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if (i>>x)&1 and (j>>y)&1 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h, w, k = map(int, input().split())
    c_list = []
    for i in range(h):
        c_list.append(input())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k1 in range(h):
                for l1 in range(w):
                    if (i >> k1) & 1 == 0 and (j >> l1) & 1 == 0 and c_list[k1][l1] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, K = map(int, input().strip().split())
    c = []
    for i in range(H):
        c.append(input())

    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if i >> k & 1 == 1 and j >> l & 1 == 1 and c[k][l] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    import sys
    from collections import Counter
    from itertools import product
    input = sys.stdin.readline

    H, W, K = map(int, input().split())
    c = [input().strip() for _ in range(H)]
    ans = 0

    for r in range(1 << H):
        for c in range(1 << W):
            cnt = sum(c[i][j] == '#' for i, j in product(range(H), range(W)) if (r >> i) & 1 and (c >> j) & 1)
            if cnt == K:
                ans += 1

    print(ans)

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    print('Hello World')
