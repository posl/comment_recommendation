Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, d = map(int, input().split())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        if x[i] ** 2 + y[i] ** 2 <= d ** 2:
            ans += 1
    print(ans)

=======
Suggestion 2

def get_distance(x,y):
    return (x**2 + y**2)**(1/2)

N,D = map(int, input().split())

count = 0
for i in range(N):
    x,y = map(int, input().split())
    distance = get_distance(x,y)
    if distance <= D:
        count += 1

print(count)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    cnt = 0
    for i in range(N):
        if pow(pow(X[i],2) + pow(Y[i],2), 1/2) <= D:
            cnt += 1

    print(cnt)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    print(len([1 for _ in range(n) if sum(map(lambda x: x**2, map(int, input().split()))) <= d**2]))

=======
Suggestion 5

def main():
    n,d = map(int,input().split())
    x = []
    y = []
    for i in range(0,n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    cnt = 0
    for i in range(0,n):
        if x[i]**2 + y[i]**2 <= d**2:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        if xy[i][0]**2 + xy[i][1]**2 <= d**2:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if (x**2+y**2)**(1/2) <= d:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**(1/2) <= D:
            count += 1
    print(count)

=======
Suggestion 10

def solve():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x**2 + y**2 <= d**2:
            count += 1
    print(count)
