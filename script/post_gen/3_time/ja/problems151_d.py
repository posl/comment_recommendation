Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx * dy != 0:
                        continue
                    if dx == dy == 0:
                        continue
                    x = i + dx
                    y = j + dy
                    if 0 <= x < H and 0 <= y < W:
                        if S[x][y] == "#":
                            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            cnt = 0
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if S[ni][nj] == "#":
                    cnt += 1
            ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(i + 1, H):
                for l in range(j + 1, W):
                    if S[k][l] == '#':
                        continue
                    ans = max(ans, abs(i - k) + abs(j - l) + 1)
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for k in range(H):
                for l in range(W):
                    if S[k][l] == "#":
                        continue
                    dist = [[-1]*W for _ in range(H)]
                    dist[i][j] = 0
                    Q = [(i, j)]
                    while Q:
                        x, y = Q.pop()
                        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                continue
                            if S[nx][ny] == "#":
                                continue
                            if dist[nx][ny] != -1:
                                continue
                            dist[nx][ny] = dist[x][y] + 1
                            Q.append((nx, ny))
                    ans = max(ans, dist[k][l])
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue

            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.':
                    ans += 1

    print(ans // 2)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            for k in range(4):
                ni = i + [1,0,-1,0][k]
                nj = j + [0,1,0,-1][k]
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.':
                    ans += 1
    print(ans//2)

=======
Suggestion 7

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
            for k in range(i, H):
                for l in range(j, W):
                    if S[k][l] == '#':
                        continue
                    ans = max(ans, abs(i - k) + abs(j - l))
    print(ans + 1)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    start = []
    goal = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                start.append((i, j))
                goal.append((i, j))
    ans = 0
    for i in range(len(start)):
        for j in range(len(goal)):
            ans = max(ans, bfs(start[i], goal[j], S))
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    dist = [[float("inf")]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            if i == 0 and j == 0:
                dist[i][j] = 0
            if i > 0:
                dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
            if j > 0:
                dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if S[i][j] == "#":
                continue
            if i < H-1:
                dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
            if j < W-1:
                dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            ans = max(ans, dist[i][j])
    print(ans)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 道のマスの数をカウント
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                cnt += 1

    # スタートとゴールのマスを決める
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                start = (i, j)
                break
        else:
            continue
        break

    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if S[i][j] == '.':
                goal = (i, j)
                break
        else:
            continue
        break

    # スタートからゴールまでの最短経路を求める
    from collections import deque
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        p = q.popleft()
        if p == goal:
            break
        for x, y in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)):
            if 0 <= x < H and 0 <= y < W and S[x][y] == '.' and dist[x][y] == -1:
                dist[x][y] = dist[p[0]][p[1]] + 1
                q.append((x, y))

    print(cnt - dist[goal[0]][goal[1]] - 1)
