def gcd(a, b):
    if a==0:
        return b
    return gcd(b%a, a)
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dy = xy[j][1] - xy[i][1]
        dx = xy[j][0] - xy[i][0]
        if dx == 0:
            continue
        if dy == 0:
            ans += 1
            continue
        if dx < 0:
            dx = -dx
            dy = -dy
        g = gcd(dx, dy)
        if g == 0:
            continue
        dy = dy//g
        dx = dx//g
        if dy > 0:
            ans += 1
print(ans)
