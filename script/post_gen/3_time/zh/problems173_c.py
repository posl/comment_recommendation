Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve(h,w,k,grid):
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for r in range(h):
                for c in range(w):
                    if ((i>>r)&1)==0 and ((j>>c)&1)==0 and grid[r][c]=='#':
                        cnt += 1
            if cnt==k:
                ans += 1
    return ans

=======
Suggestion 3

def check(lst):
    count = 0
    for i in range(H):
        for j in range(W):
            if lst[i][j] == '#':
                count += 1
    if count == K:
        return True
    else:
        return False

=======
Suggestion 4

def count_black(s):
    return sum([1 if c == '#' else 0 for c in s])

=======
Suggestion 5

def dfs(x, y, k, a, b, c):
    if x == 0:
        if k == 0:
            return 1
        else:
            return 0
    if y == 0:
        return dfs(x - 1, b, k, a, b, c)
    if c[x - 1][y - 1] == "#":
        return dfs(x, y - 1, k - 1, a, b, c) + dfs(x, y - 1, k, a, b, c)
    else:
        return dfs(x, y - 1, k, a, b, c)

=======
Suggestion 6

def dfs(h, w, k, i, j, k2, w2, h2):
    if i == h:
        if k2 == k:
            return 1
        else:
            return 0
    if j == w:
        return dfs(h, w, k, i + 1, 0, k2, w2, h2)
    if k2 + w2[i] + h2[j] > k:
        return dfs(h, w, k, i, j + 1, k2, w2, h2)
    return dfs(h, w, k, i, j + 1, k2, w2, h2) + dfs(h, w, k, i + 1, j, k2 + 1, w2, h2)

=======
Suggestion 7

def dfs(i,j,black):
    if i == H:
        if black == K:
            return 1
        else:
            return 0
    if j == W:
        return dfs(i+1,0,black)
    ret = 0
    ret += dfs(i,j+1,black)
    ret += dfs(i,j+1,black+1)
    return ret

H,W,K = map(int,input().split())
c = [list(input()) for _ in range(H)]
print(dfs(0,0,0))
