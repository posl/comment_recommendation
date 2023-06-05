def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        if dx == 0 or dy == 0:
            continue
        if dx * dy > 0:
            continue
        if abs(dx) > abs(dy):
            dx, dy = dy, dx
        if dx < 0:
            dx, dy = -dx, -dy
        g = gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g
        if dx > 0:
            ans += 1
print(ans)
