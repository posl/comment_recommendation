def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        if dx == 0:
            ans += 1
        else:
            if dx < 0:
                dx *= -1
                dy *= -1
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            if -dy <= dx and dx <= dy:
                ans += 1
print(ans)
