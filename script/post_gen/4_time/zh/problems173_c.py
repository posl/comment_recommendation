Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    print("Hello World!")

=======
Suggestion 3

def p173_c():
    pass

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    c = []
    for i in range(H):
        c.append(list(input()))

    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            black = 0
            for k in range(H):
                for l in range(W):
                    if i>>k & 1 and j>>l & 1 and c[k][l] == '#':
                        black += 1
            if black == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def dfs(i, j, k, h, w, c):
    if i == h:
        return k == 0
    if j == w:
        return dfs(i + 1, 0, k, h, w, c)
    if c[i][j] == '#':
        return dfs(i, j + 1, k - 1, h, w, c)
    return dfs(i, j + 1, k, h, w, c) + dfs(i, j + 1, k - 1, h, w, c)

=======
Suggestion 6

def solve():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for k in range(H):
                for l in range(W):
                    if (i >> k & 1) == 0 and (j >> l & 1) == 0 and c[k][l] == '#':
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

solve()
