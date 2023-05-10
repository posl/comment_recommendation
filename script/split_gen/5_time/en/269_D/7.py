def main():
    N = int(input())
    black = set()
    for _ in range(N):
        x, y = map(int, input().split())
        black.add((x, y))
    ans = 0
    while black:
        ans += 1
        q = [black.pop()]
        while q:
            x, y = q.pop()
            for dx, dy in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
                if (x+dx, y+dy) in black:
                    q.append((x+dx, y+dy))
                    black.remove((x+dx, y+dy))
    print(ans)
