def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dy = y[i] - y[j]
        dx = x[i] - x[j]
        if dy == 0:
            ans += 1
        elif dx == 0:
            continue
        else:
            if dx < 0:
                dx = -dx
                dy = -dy
            g = gcd(dx, dy)
            dx = dx//g
            dy = dy//g
            if dx <= dy:
                ans += 1
print(ans)
