def main():
    from sys import stdin
    from collections import deque
    r1, c1 = map(int, stdin.readline().split())
    r2, c2 = map(int, stdin.readline().split())
    q = deque()
    q.append((r1, c1, 0))
    visited = set()
    visited.add((r1, c1))
    while q:
        r, c, d = q.popleft()
        if r == r2 and c == c2:
            print(d)
            return
        for dr in range(-3, 4):
            for dc in range(-3, 4):
                if abs(dr) + abs(dc) <= 3:
                    nr = r + dr
                    nc = c + dc
                    if (nr, nc) not in visited:
                        q.append((nr, nc, d + 1))
                        visited.add((nr, nc))
