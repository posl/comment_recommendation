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
                ans = max(ans, bfs(S, i, j))
    print(ans)

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                cnt = 0
                if i > 0 and s[i-1][j] == ".":
                    cnt += 1
                if i < h-1 and s[i+1][j] == ".":
                    cnt += 1
                if j > 0 and s[i][j-1] == ".":
                    cnt += 1
                if j < w-1 and s[i][j+1] == ".":
                    cnt += 1
                ans += 4 - cnt
    print(ans)

main()

=======
Suggestion 3

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans += 1
    if ans == H * W:
        print(ans - 1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    print(ans-1)

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans += 1
    if ans == h*w:
        print(ans-1)
    else:
        print(ans)

=======
Suggestion 6

def maze():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    if ans == h * w:
        return ans - 1
    else:
        return ans

print(maze())

=======
Suggestion 7

def solve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    max_cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue

            # スタート地点を決める
            start = (i, j)

            # ゴール地点を決める
            for k in range(H):
                for l in range(W):
                    if S[k][l] == '#':
                        continue
                    goal = (k, l)

                    # BFSで最短距離を求める
                    dist = [[-1] * W for _ in range(H)]
                    dist[start[0]][start[1]] = 0
                    queue = [start]
                    while queue:
                        x, y = queue.pop(0)
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx = x + dx
                            ny = y + dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                continue
                            if S[nx][ny] == '#':
                                continue
                            if dist[nx][ny] != -1:
                                continue
                            dist[nx][ny] = dist[x][y] + 1
                            queue.append((nx, ny))

                    max_cnt = max(max_cnt, dist[goal[0]][goal[1]])

    print(max_cnt)

=======
Suggestion 8

def solve():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if i == 0 and j == w-1:
                continue
            if i == h-1 and j == 0:
                continue
            if i == h-1 and j == w-1:
                continue
            if s[i][j] == '.':
                ans += 1
    print(ans*2)

=======
Suggestion 9

def get_max_move_count(h, w, s):
    max_move_count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            move_count = 0
            for k in range(h):
                for l in range(w):
                    if s[k][l] == '#':
                        continue
                    move_count = max(move_count, abs(i - k) + abs(j - l))
            max_move_count = max(max_move_count, move_count)
    return max_move_count

=======
Suggestion 10

def check(x, y, H, W):
    if x < 0 or W <= x or y < 0 or H <= y:
        return False
    return True
