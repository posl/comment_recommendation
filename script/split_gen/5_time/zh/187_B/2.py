def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dx = xy[i][0] - xy[j][0]
        dy = xy[i][1] - xy[j][1]
        if dx == 0:
            ans += 1
            continue
        if dy == 0:
            continue
        g = gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g
        if dx < 0:
            dx = -dx
            dy = -dy
        if dx == 1 and dy == 1:
            ans += 1
        elif dx == -1 and dy == 1:
            ans += 1
        elif dx == 1 and dy == -1:
            ans += 1
        elif dx == -1 and dy == -1:
            ans += 1
print(ans)
