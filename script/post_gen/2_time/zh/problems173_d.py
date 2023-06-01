Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve(h, w, k, c):
    ans = 0
    for i in range(1 << h):
        for j in range(1 << w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    return ans


h, w, k = map(int, input().split())
c = [input() for i in range(h)]
print(solve(h, w, k, c))

=======
Suggestion 3

def main():
    h, w, k = map(int, input().split())
    c = []
    for _ in range(h):
        c.append(list(input()))
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for l in range(h):
                for m in range(w):
                    if (i >> l) & 1 == 0 and (j >> m) & 1 == 0 and c[l][m] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

=======
Suggestion 4

def get_input():
    h, w, k = map(int, input().split(" "))
    c = []
    for i in range(h):
        c.append(list(input()))
    return h, w, k, c

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    c = []
    for _ in range(H):
        c.append(input())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if (i>>k)&1 and (j>>l)&1 and c[k][l] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            black = 0
            for k in range(h):
                for l in range(w):
                    if i >> k & 1 and j >> l & 1 and c[k][l] == '#':
                        black += 1
            if black == k:
                ans += 1
    print(ans)
