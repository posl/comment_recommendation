def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dy = points[i][1] - points[j][1]
        dx = points[i][0] - points[j][0]
        if dy == 0:
            ans += 1
        elif dx == 0:
            continue
        else:
            if dx < 0:
                dy = -dy
                dx = -dx
            g = gcd(abs(dy), abs(dx))
            dy //= g
            dx //= g
            if dy <= dx:
                ans += 1
print(ans)

if __name__ == '__main__':
    gcd()