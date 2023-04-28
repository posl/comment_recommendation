Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 % 1 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for d in range(D):
                dist += (X[i][d] - X[j][d])**2
            dist = dist**0.5
            if int(dist) == dist:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            tmp = 0
            for k in range(d):
                tmp += (x[i][k] - x[j][k]) ** 2
            if tmp ** 0.5 == int(tmp ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if (dist ** 0.5).is_integer():
                ans += 1

    print(ans)

=======
Suggestion 5

def main():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            tmp = 0
            for k in range(d):
                tmp += (x[i][k] - x[j][k])**2
            tmp = tmp**0.5
            if tmp.is_integer():
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if dist**0.5 % 1 == 0:
                ans += 1
    print(ans)

=======
Suggestion 7

def get_input():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    return N, D, X

=======
Suggestion 8

def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])**2
    return d

n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j])**0.5 % 1 == 0:
            ans += 1

print(ans)

=======
Suggestion 9

def getDistance(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist ** 0.5

n, d = map(int, input().split())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if getDistance(points[i], points[j]).is_integer():
            ans += 1

print(ans)

=======
Suggestion 10

def main():
    print("Hello World")
