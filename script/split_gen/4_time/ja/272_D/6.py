def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    if M == 1:
        print("\n".join(" ".join(str(i + j) for j in range(N)) for i in range(N)))
        return
    sq = int(M ** 0.5)
    if sq * sq == M:
        sq -= 1
    sq += 1
    sq2 = sq * sq
    dist = [[-1] * N for _ in range(N)]
    dist[0][0] = 0
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        for dx, dy in ((-sq, 0), (sq, 0), (0, -sq), (0, sq)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
    print("\n".join(" ".join(str(dist[i][j]) for j in range(N)) for i in range(N)))
