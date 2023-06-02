Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_y = input().split()
        x.append(int(x_y[0]))
        y.append(int(x_y[1]))
    # print(x)
    # print(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (y[i]-y[j])/(x[i]-x[j]) >= -1 and (y[i]-y[j])/(x[i]-x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 2

def get_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs((y[j]-y[i])/(x[j]-x[i])) <= 1:
                count += 1
    print(count)

=======
Suggestion 5

def cal(n, x, y):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            k = (y[i]-y[j])/(x[i]-x[j])
            if k >= -1 and k <= 1:
                cnt += 1
    return cnt

n = int(input())
x = []
y = []
for i in range(n):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)
print(cal(n, x, y))

=======
Suggestion 6

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

=======
Suggestion 7

def main():
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
            if -1 <= (y[j] - y[i])/(x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1
    print(count)
