def search(x, y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x, y) in black:
        return
    black.add((x, y))
    search(x - 1, y - 1)
    search(x - 1, y)
    search(x, y - 1)
    search(x, y + 1)
    search(x + 1, y)
    search(x + 1, y + 1)
n = int(input())
black = set()
for _ in range(n):
    x, y = map(int, input().split())
    search(x, y)
print(len(black))
