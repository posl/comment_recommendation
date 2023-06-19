Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 2

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x%y)

=======
Suggestion 3

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

=======
Suggestion 4

def gcd(x, y):
    if x == 0 or y == 0:
        return 0
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

=======
Suggestion 5

def solve(n, x, y):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(y[i] - y[j]) <= abs(x[i] - x[j]):
                res += 1
    return res

=======
Suggestion 6

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    # print(points)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 7

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
xy = []
for _ in range(n):
    xy.append(tuple(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if abs(xy[i][0]-xy[j][0]) >= abs(xy[i][1]-xy[j][1]):
            ans += 1

print(ans)
