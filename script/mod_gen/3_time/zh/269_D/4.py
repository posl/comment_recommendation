def find(x, y):
    if (x, y) in black:
        black.remove((x, y))
        find(x - 1, y - 1)
        find(x - 1, y)
        find(x, y - 1)
        find(x, y + 1)
        find(x + 1, y)
        find(x + 1, y + 1)
        return True
    return False
n = int(input())
black = set()
for _ in range(n):
    x, y = map(int, input().split())
    black.add((x, y))
ans = 0
while black:
    x, y = black.pop()
    if find(x, y):
        ans += 1
print(ans)

if __name__ == '__main__':
    find()