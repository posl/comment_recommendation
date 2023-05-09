Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                from collections import deque
                d = [[-1] * w for _ in range(h)]
                d[i][j] = 0
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()
                    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] == "." and d[ny][nx] == -1:
                            d[ny][nx] = d[y][x] + 1
                            q.append((ny, nx))
                ans = max(ans, max(map(max, d)))
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans = max(ans, bfs(i, j, H, W, S))
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(ans, bfs(H, W, S, i, j))
    print(ans)

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                #print(i,j)
                dist = [[-1] * W for _ in range(H)]
                dist[i][j] = 0
                q = [(i,j)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and dist[nx][ny] == -1:
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
                ans = max(ans, max([max(d) for d in dist]))
    print(ans)
solve()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(ans, solve(H, W, S, i, j))
    print(ans)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(S)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    max_road = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                max_road += 1
    print(max_road - 2)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    print(S)
    print(H)
    print(W)
    print(S[0][0])
    print(S[0][1])
    print(S[1][0])
    print(S[1][1])
    print(S[2][0])
    print(S[2][1])
    print(S[2][2])
    print(S[1][2])
    print(S[0][2])
    print(S[0][3])
    print(S[1][3])
    print(S[2][3])
    print(S[2][4])
    print(S[1][4])
    print(S[0][4])

    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[1][2])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[1][3])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[1][4])
    #print(S[0][4])

    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[1][2])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[1][3])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[1][4])
    #print(S[0][4])

    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    print(S)
    print(H, W)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]

    #print(S)

    # 1. count the number of '.'s
    count = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                count += 1

    # 2. find the maximum distance from any '.' to any '.'
    max_dist = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                dist = 0
                for hh in range(H):
                    for ww in range(W):
                        if S[hh][ww] == '.':
                            dist = max(dist, abs(h-hh) + abs(w-ww))
                max_dist = max(max_dist, dist)

    #print(count, max_dist)

    print(max_dist)
