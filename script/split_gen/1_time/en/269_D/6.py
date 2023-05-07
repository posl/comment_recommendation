def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    n = int(input())
    xd = [0, 0, 1, 1, -1, -1]
    yd = [-1, 1, -1, 0, 0, 1]
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy = set(xy)
    visited = set()
    ans = 0
    for x, y in xy:
        if (x, y) in visited:
            continue
        ans += 1
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            visited.add((x, y))
            for dx, dy in zip(xd, yd):
                nx, ny = x + dx, y + dy
                if (nx, ny) in xy and (nx, ny) not in visited:
                    q.append((nx, ny))
    print(ans)
