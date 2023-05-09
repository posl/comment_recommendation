Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            a = x[i] - x[j]
            b = y[i] - y[j]
            count = 0
            for k in range(N):
                for l in range(k+1, N):
                    if x[k] - x[l] == a and y[k] - y[l] == b:
                        count += 1
            ans = max(ans, N - count)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            x1 = x[j] - x[i]
            y1 = y[j] - y[i]
            ans = max(ans, (x1**2 + y1**2)**0.5)

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if abs(x[i]-x[j]) >= abs(y[i]-y[j]):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, abs(xy[i][0]-xy[j][0])+abs(xy[i][1]-xy[j][1]))
    print(ans)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def solve():
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = towns[i]
            x2, y2 = towns[j]
            dx = x2 - x1
            dy = y2 - y1
            cnt = 0
            for k in range(N):
                x3, y3 = towns[k]
                if (x3+dx, y3+dy) in towns:
                    cnt += 1
            ans = max(ans, cnt)
    print(N-ans)

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort()
xy = [[xy[i][0]-xy[0][0], xy[i][1]-xy[0][1]] for i in range(n)]
ans = 10**9
for i in range(n):
    for j in range(i+1, n):
        x = xy[i][0]-xy[j][0]
        y = xy[i][1]-xy[j][1]
        ans = min(ans, gcd(x,y))
print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def get_ab(x1, y1, x2, y2):
        a = x2 - x1
        b = y2 - y1
        g = gcd(a, b)
        a //= g
        b //= g
        return (a, b)

    ab = set()
    for i in range(N):
        for j in range(i + 1, N):
            ab.add(get_ab(XY[i][0], XY[i][1], XY[j][0], XY[j][1]))
    print(len(ab) + 1)

=======
Suggestion 9

def main():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    l = sorted(l, key=lambda x: (x[0], x[1]))
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            dx = l[j][0] - l[i][0]
            dy = l[j][1] - l[i][1]
            if (dx, dy) in d:
                d[(dx, dy)] += 1
            else:
                d[(dx, dy)] = 1
    mx = 0
    for v in d.values():
        mx = max(mx, v)
    print(n-mx)

=======
Suggestion 10

def solve():
    pass
