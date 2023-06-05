Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if points[i][0] == points[j][0]:
                continue
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    return b

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 5

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(i+1, N):
        if abs(points[i][0] - points[j][0]) <= abs(points[i][1] - points[j][1]):
            count += 1
print(count)

=======
Suggestion 6

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

=======
Suggestion 7

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

=======
Suggestion 8

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
