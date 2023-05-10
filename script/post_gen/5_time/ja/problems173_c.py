Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]

    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0 and c[k][l] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1

    print(ans)

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]
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
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]

    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0 and C[k][l] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    C = [input() for i in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 and (j >> l) & 1 and C[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i >> k & 1:
                        continue
                    if j >> l & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if (i>>k)&1 == 0 and (j>>l)&1 == 0 and c[k][l] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    H, W, K = map(int, input().split())
    c = []
    for i in range(H):
        c.append(list(input()))

    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and c[h][w] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]

    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0 and C[k][l] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
