def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))
ans = 0
for i in range(n):
    d = {}
    for j in range(n):
        if i != j:
            dx = p[i][0] - p[j][0]
            dy = p[i][1] - p[j][1]
            if dx == 0:
                dy = 1
            elif dy == 0:
                dx = 1
            else:
                if dx < 0:
                    dx = -dx
                    dy = -dy
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
            if (dx, dy) in d:
                d[(dx, dy)] += 1
            else:
                d[(dx, dy)] = 1
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
print(ans // 2)
