def main():
    n = int(input())
    black = set()
    for i in range(n):
        x, y = map(int, input().split())
        black.add((x, y))
    ans = 0
    while len(black) > 0:
        ans += 1
        x, y = black.pop()
        q = [(x, y)]
        while len(q) > 0:
            x, y = q.pop()
            if (x - 1, y - 1) in black:
                black.remove((x - 1, y - 1))
                q.append((x - 1, y - 1))
            if (x - 1, y) in black:
                black.remove((x - 1, y))
                q.append((x - 1, y))
            if (x, y - 1) in black:
                black.remove((x, y - 1))
                q.append((x, y - 1))
            if (x, y + 1) in black:
                black.remove((x, y + 1))
                q.append((x, y + 1))
            if (x + 1, y) in black:
                black.remove((x + 1, y))
                q.append((x + 1, y))
            if (x + 1, y + 1) in black:
                black.remove((x + 1, y + 1))
                q.append((x + 1, y + 1))
    print(ans)

if __name__ == '__main__':
    main()