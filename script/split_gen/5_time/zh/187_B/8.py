def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        dx, dy = x2 - x1, y2 - y1
        if dx == 0:
            if dy == 0:
                continue
            else:
                ans += 1
        else:
            if dy == 0:
                ans += 1
            else:
                if dx < 0:
                    dx, dy = -dx, -dy
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if -dx <= dy <= dx:
                    ans += 1
print(ans)
