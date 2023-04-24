Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(1 << h):
        for j in range(1 << w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if i >> x & 1 and j >> y & 1 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(1 << h):
        for j in range(1 << w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if i >> x & 1 == 0 and j >> y & 1 == 0 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i>>k)&1 and (j>>l)&1 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
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
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    c = []
    for i in range(H):
        c.append(input())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if i>>k&1 == 0 and j>>l&1 == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())

    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if (i>>x)&1 == 0 and (j>>y)&1 == 0 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    H, W, K = map(int, input().split())
    c = []
    for i in range(H):
        c.append(list(input()))

    ans = 0
    for i in range(1<<H):
        for j in range(1<<W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if ((i>>k)&1)==0 and ((j>>l)&1)==0 and c[k][l]=="#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)
    return 0

=======
Suggestion 8

def get_input_data():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    return h, w, k, c

=======
Suggestion 9

def main():
    H, W, K = map(int, input().split())
    c = []
    for _ in range(H):
        c.append(input())
    #print(c)
    ans = 0
    for h in range(1 << H):
        for w in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if (h >> i & 1) == 0 and (w >> j & 1) == 0 and c[i][j] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

=======
Suggestion 10

def check(a, h, w, k):
    ret = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                ret += 1
    return ret == k
