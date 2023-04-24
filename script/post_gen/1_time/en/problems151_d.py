Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans = max(ans, bfs(s, i, j))
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans = max(ans, dfs(s, i, j, h, w))
    print(ans)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans = max(ans, bfs(s, i, j, h, w))
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            stack = [[i,j]]
            visited = [[False for _ in range(W)] for _ in range(H)]
            visited[i][j] = True
            while len(stack) > 0:
                x, y = stack.pop()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= H or ny < 0 or ny >= W:
                        continue
                    if visited[nx][ny]:
                        continue
                    if S[nx][ny] == '#':
                        continue
                    visited[nx][ny] = True
                    stack.append([nx, ny])
            tmp = 0
            for k in range(H):
                for l in range(W):
                    if visited[k][l]:
                        tmp += 1
            ans = max(ans, tmp)
    print(ans-1)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    max_path = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                max_path = max(max_path, bfs(H, W, S, i, j))
    print(max_path)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    max_count = 0

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                for k in range(H):
                    for l in range(W):
                        if S[k][l] == '.':
                            dist = abs(k - i) + abs(l - j)
                            max_count = max(max_count, dist)

    print(max_count)

=======
Suggestion 7

def main():
    H,W = map(int, input().split())
    S = [ input() for i in range(H) ]
    result = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                result = max(result, solve(H, W, S, i, j))
    print(result)

=======
Suggestion 8

def func(h,w,ls):
    max_ = 0
    for i in range(h):
        for j in range(w):
            if ls[i][j] == '#':
                continue
            visited = [[False]*w for _ in range(h)]
            visited[i][j] = True
            stack = [(i,j,0)]
            while stack:
                x,y,cnt = stack.pop()
                max_ = max(max_,cnt)
                for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0 <= nx < h and 0 <= ny < w and ls[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx,ny,cnt+1))
    return max_

=======
Suggestion 9

def main():
    pass
