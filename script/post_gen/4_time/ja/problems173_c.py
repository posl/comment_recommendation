Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if ((i >> x) & 1) == 0 and ((j >> y) & 1) == 0 and c[x][y] == "#":
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if i>>k&1 and j>>l&1 and c[k][l] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if i>>x&1==0 and j>>y&1==0 and c[x][y]=='#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
main()

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0:
                        if c[k][l] == '#':
                            black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k) & 1 == 0 and (j >> l) & 1 == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(1<<h):
        for j in range(1<<w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if i>>x&1 or j>>y&1:
                        continue
                    if c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1<<H):
        for j in range(1<<W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i>>k & 1:
                        continue
                    if j>>l & 1:
                        continue
                    if c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    H,W,K = map(int,input().split())
    c = [input() for i in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if ((i>>k)&1)==0 and ((j>>l)&1)==0 and c[k][l]=='#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 9

def dfs(i, j, n, m, k, c):
    if i == n and j == m:
        if k == 0:
            return 1
        else:
            return 0
    if c[i][j] == '#':
        return dfs(i + 1, j, n, m, k, c)
    else:
        c1 = dfs(i + 1, j, n, m, k - 1, c)
        c2 = dfs(i, j + 1, n, m, k - 1, c)
        return c1 + c2

=======
Suggestion 10

def main():
    pass
