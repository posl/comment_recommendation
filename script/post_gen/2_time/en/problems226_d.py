Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

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
    while b:
        a, b = b, a % b
    return a

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
    ans = 0
    for i in range(N):
        for j in range(i):
            a = x[i] - x[j]
            b = y[i] - y[j]
            a2 = x[j] - x[i]
            b2 = y[j] - y[i]
            count = 0
            for k in range(N):
                if x[k] == x[i] + a and y[k] == y[i] + b:
                    count += 1
                if x[k] == x[i] + a2 and y[k] == y[i] + b2:
                    count += 1
            ans = max(ans, count)
    print(N - ans)

=======
Suggestion 5

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    dist = []
    for i in range(N-1):
        dist.append(X[i+1]-X[i])
        dist.append(Y[i+1]-Y[i])
    dist.sort()
    ans = 0
    for i in range(N-1):
        ans += dist[i]*(N-1-i)
    print(ans)
main()

=======
Suggestion 6

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            S.add((x2-x1, y2-y1))
            S.add((x1-x2, y1-y2))
    print(len(S))

=======
Suggestion 7

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
            ans = max(ans,abs(x[i]-x[j])+abs(y[i]-y[j]))
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY.sort()
    X = [xy[0] for xy in XY]
    Y = [xy[1] for xy in XY]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, abs(X[i]-X[j])+abs(Y[i]-Y[j]))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            if (x1 - dx, y1 - dy) not in points:
                ans += 1
            if (x2 + dx, y2 + dy) not in points:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    X,Y = [],[]
    for i in range(N):
        a,b = map(int,input().split())
        X.append(a)
        Y.append(b)
    ans = set()
    for i in range(N):
        for j in range(i+1,N):
            ans.add((X[i]-X[j],Y[i]-Y[j]))
            ans.add((X[j]-X[i],Y[j]-Y[i]))
    print(len(ans))

main()
