def check(x, y):
    if x >= 0 and x < w and y >= 0 and y < h and grid[y][x] == '.':
        return True
    return False
h, w = map(int, input().split())
grid = [input() for _ in range(h)]
ans = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == '.':
            ans += 1
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                grid[y][x] = '#'
                for dx, dy in [(1, 0), (0, 1)]:
                    if check(x + dx, y + dy):
                        stack.append((x + dx, y + dy))
print(ans)

if __name__ == '__main__':
    check()