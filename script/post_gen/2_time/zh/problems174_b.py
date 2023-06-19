Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,d = map(int,input().split())
    count = 0
    for i in range(n):
        x,y = map(int,input().split())
        if x**2 + y**2 <= d**2:
            count += 1
    print(count)

=======
Suggestion 2

def get_distance(x, y):
    return pow(pow(x, 2) + pow(y, 2), 0.5)

n, d = map(int, input().split())
count = 0
for i in range(n):
    x, y = map(int, input().split())
    if get_distance(x, y) <= d:
        count += 1
print(count)

=======
Suggestion 3

def problem174_b():
    #读入数据
    N,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    #计算距离
    distance = []
    for i in range(N):
        distance.append((X[i]**2+Y[i]**2)**(1/2))
    #判断是否在圆内
    count = 0
    for i in range(N):
        if distance[i] <= D:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        if X[i] ** 2 + Y[i] ** 2 <= D ** 2:
            ans += 1
    print(ans)

=======
Suggestion 5

def f1(n,d,x,y):
    n = int(n)
    d = int(d)
    x = int(x)
    y = int(y)
    r = 0
    for i in range(n):
        if (x[i]**2 + y[i]**2)**0.5 <= d:
            r += 1
    return r

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X**2 + Y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 7

def solve():
    n, d = map(int, input().split())
    cnt = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x*x + y*y <= d*d:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n,d = map(int,input().split())
    ans = 0
    for i in range(n):
        x,y = map(int,input().split())
        if (x**2+y**2)**0.5 <= d:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n,d = map(int,input().split())
    cnt = 0
    for i in range(n):
        x,y = map(int,input().split())
        if d**2 >= x**2 + y**2:
            cnt += 1
    print(cnt)
