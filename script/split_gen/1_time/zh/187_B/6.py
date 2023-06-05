def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dx, dy = x2 - x1, y2 - y1
        if dx == 0:
            ans += 1
            continue
        if dy == 0:
            ans += 1
            continue
        g = gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g
        if dx < 0:
            dx *= -1
            dy *= -1
        if dx > 0 and dy > 0:
            ans += 1
print(ans)
