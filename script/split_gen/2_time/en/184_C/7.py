def main():
    from collections import deque
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    visited = set()
    visited.add((r1, c1))
    q = deque()
    q.append((r1, c1, 0))
    while q:
        r, c, d = q.popleft()
        if r == r2 and c == c2:
            print(d)
            return
        for nr, nc in [(r + 2, c + 1), (r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1), (r + 1, c + 2), (r + 1, c - 2), (r - 1, c + 2), (r - 1, c - 2)]:
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, d + 1))
