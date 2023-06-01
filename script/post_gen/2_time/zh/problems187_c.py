Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    # 读入数据
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    # 斜率的范围是[-1, 1]，即-1 <= (y2 - y1) / (x2 - x1) <= 1
    # 两边同时乘以(x2 - x1)，则-1 * (x2 - x1) <= y2 - y1 <= 1 * (x2 - x1)
    # 移项得-1 * (x2 - x1) - y2 + y1 <= 0 <= 1 * (x2 - x1) - y2 + y1
    # 所以对于每个点，只要找到与其连线的斜率在[-1, 1]的点的数目即可
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if -1 * (x2 - x1) - y2 + y1 <= 0 <= 1 * (x2 - x1) - y2 + y1:
                count += 1
    print(count)

=======
Suggestion 2

def is_slope_in_1_to_minus1(x1,y1,x2,y2):
    return abs((y2-y1)/(x2-x1))<=1

=======
Suggestion 3

def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return float('inf')
    else:
        return (y2 - y1) / (x2 - x1)

=======
Suggestion 4

def get_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return 0
    return (y2 - y1) / (x2 - x1)

=======
Suggestion 5

def count_slope(a, b):
    if a[0] - b[0] == 0:
        return 0
    else:
        return (a[1] - b[1]) / (a[0] - b[0])

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(0)
        y.append(0)
    for i in range(n):
        a, b = map(int, input().split())
        x[i] = a
        y[i] = b
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[i]-y[j]) / (x[i]-x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x = xy[i][0] - xy[j][0]
        y = xy[i][1] - xy[j][1]
        if x == 0:
            ans += 1
        else:
            if x < 0:
                x *= -1
                y *= -1
            g = gcd(x, y)
            x //= g
            y //= g
            if -1 <= y <= 1:
                ans += 1
print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if abs(points[i][0] - points[j][0]) <= abs(points[i][1] - points[j][1]):
            cnt += 1
print(cnt)

=======
Suggestion 10

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
