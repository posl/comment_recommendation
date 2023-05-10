def solve():
    from sys import stdin
    input = stdin.readline
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    from collections import deque
    q = deque([(ch - 1, cw - 1)])
    visited = [[False] * w for _ in range(h)]
    visited[ch - 1][cw - 1] = True
    d = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == dh - 1 and j == dw - 1:
                print(d)
                return
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj))
        d += 1
        for i in range(max(0, ch - 3), min(h, ch + 2)):
            for j in range(max(0, cw - 3), min(w, cw + 2)):
                if s[i][j] == '.' and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))
    print(-1)
solve()

if __name__ == '__main__':
    solve()