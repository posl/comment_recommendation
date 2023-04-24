Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for x in range(H):
                for y in range(W):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and C[x][y] == "#":
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
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for h in range(2**H):
        for w in range(2**W):
            black = 0
            for i in range(H):
                for j in range(W):
                    if (h>>i)&1 or (w>>j)&1:
                        continue
                    if C[i][j] == "#":
                        black += 1
            if black == K:
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
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if ((i >> h) & 1) == 0 and ((j >> w) & 1) == 0 and C[h][w] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and C[h][w] == "#":
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
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and c[i][j] == '#':
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
    for i in range(2 ** H):
        for j in range(2 ** W):
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if (i >> h) & 1 == 0 and (j >> w) & 1 == 0 and c[h][w] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H, W, K = map(int, input().split())
    s = [input() for _ in range(H)]
    ans = 0
    for h in range(2 ** H):
        for w in range(2 ** W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i) & 1 == 0 and (w >> j) & 1 == 0 and s[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    # 入力
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]

    # 何行選ぶかの組み合わせを全探索
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    # このマスを選んでいるか
                    is_selected = (i >> x) & 1 == 0 and (j >> y) & 1 == 0
                    if is_selected and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1

    # 出力
    print(ans)
