Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
        if abs(x[i] - x[j]) <= abs(y[i] - y[j]):
            ans += 1

print(ans)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    slopes = {}
    for j in range(n):
        if i == j:
            continue
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        if dx == 0:
            slope = float('inf')
        else:
            slope = dy / dx
        if slope not in slopes:
            slopes[slope] = 0
        slopes[slope] += 1
    for slope in slopes:
        ans += slopes[slope] * (slopes[slope] - 1) // 2

print(ans // 2)

=======
Suggestion 5

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[i][1]-points[j][1])/(points[i][0]-points[j][0]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 6

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

=======
Suggestion 7

def get_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

=======
Suggestion 8

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        dx = x[i]-x[j]
        dy = y[i]-y[j]
        if dx<0:
            dx = -dx
            dy = -dy
        if dx==0:
            dy = abs(dy)
        else:
            g = gcd(dx,dy)
            dx = dx//g
            dy = dy//g
        if dx>=-dy and dx<=dy:
            ans += 1
print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
    
ans = 0
for i in range(n):
    for j in range(i+1, n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        if dx == 0:
            ans += 1
        else:
            if dy == 0:
                ans += 1
            else:
                if dx * dy > 0:
                    ans += 1
                else:
                    if abs(dx) >= abs(dy):
                        ans += 1
print(ans)
