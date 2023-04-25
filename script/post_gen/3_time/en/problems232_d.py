Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    c = []
    for i in range(h):
        c.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())

    count = 1
    i = 0
    j = 0
    while(i < h-1 or j < w-1):
        if i < h-1 and c[i+1][j] == ".":
            count += 1
            i += 1
        elif j < w-1 and c[i][j+1] == ".":
            count += 1
            j += 1
        else:
            break

    print(count)

=======
Suggestion 5

def main():
    # Take input Here and Call solution function
    h,w = get_ints_in_variables()
    grid = []
    for i in range(h):
        grid.append(get_string())
    print(solution(h,w,grid))

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    count = 1
    i = j = 0
    while i < h and j < w:
        if i == h - 1 and j == w - 1:
            break
        if i + 1 < h and c[i + 1][j] == '.':
            i += 1
        elif j + 1 < w and c[i][j + 1] == '.':
            j += 1
        else:
            break
        count += 1
    print(count)

=======
Suggestion 7

def count():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[H-1][W-1]

print(count())

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    print(H * W - sum(row.count('#') for row in grid))

=======
Suggestion 9

def main():
  h, w = map(int, input().split())
  a = [input() for i in range(h)]
  visited = [[0]*w for i in range(h)]
  def dfs(i, j):
    if i < 0 or h <= i or j < 0 or w <= j or a[i][j] == "#":
      return
    if visited[i][j]:
      return
    visited[i][j] = 1
    dfs(i+1, j)
    dfs(i, j+1)
  dfs(0, 0)
  print(sum(sum(l) for l in visited))

=======
Suggestion 10

def get_input():
    import sys
    return sys.stdin.readline().strip()
