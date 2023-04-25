Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans = max(ans, bfs(i, j, S))
    print(ans)

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            dist = [[-1] * W for _ in range(H)]
            dist[i][j] = 0
            queue = [(i, j)]
            for x, y in queue:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < H and 0 <= ny < W):
                        continue
                    if S[nx][ny] == '#':
                        continue
                    if dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
            ans = max(ans, max(max(row) for row in dist))
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, bfs(h, w, H, W, S))
    print(ans)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    maze = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '.':
                ans = max(ans, dfs(i, j, maze))
    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    max = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                count = 0
                for k in range(h):
                    for l in range(w):
                        if s[k][l] == '.':
                            count += 1
                if count > max:
                    max = count
    print(max)

=======
Suggestion 6

def readinput():
    h,w=list(map(int,input().split()))
    s=[]
    for _ in range(h):
        si=input()
        s.append(si)
    return h,w,s

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]
    max_move = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                max_move = max(max_move, max_move_from(i, j, s))
    print(max_move)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(H, W, S)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(h*w - sum([s[i].count('#') for i in range(h)]))

=======
Suggestion 10

def solve():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(H, W)
    print(S)
    print(S[0][0])
    print(S[0][1])
    print(S[0][2])
    print(S[1][0])
    print(S[1][1])
    print(S[1][2])
    print(S[2][0])
    print(S[2][1])
    print(S[2][2])
