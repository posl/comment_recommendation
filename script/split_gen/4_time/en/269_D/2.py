def main():
    N = int(input())
    black = set()
    for _ in range(N):
        x, y = map(int, input().split())
        black.add((x, y))
    ans = 0
    while black:
        ans += 1
        x, y = black.pop()
        queue = [(x, y)]
        while queue:
            x, y = queue.pop()
            if (x-1, y-1) in black:
                black.remove((x-1, y-1))
                queue.append((x-1, y-1))
            if (x-1, y) in black:
                black.remove((x-1, y))
                queue.append((x-1, y))
            if (x, y-1) in black:
                black.remove((x, y-1))
                queue.append((x, y-1))
            if (x, y+1) in black:
                black.remove((x, y+1))
                queue.append((x, y+1))
            if (x+1, y) in black:
                black.remove((x+1, y))
                queue.append((x+1, y))
            if (x+1, y+1) in black:
                black.remove((x+1, y+1))
                queue.append((x+1, y+1))
    print(ans)
