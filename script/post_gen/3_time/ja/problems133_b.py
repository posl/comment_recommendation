Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for d in range(D):
                dist += (X[i][d] - X[j][d]) ** 2
            dist = int(dist ** 0.5)
            if dist ** 2 == dist:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if (dist**0.5).is_integer():
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            sum = 0
            for k in range(d):
                sum += (x[i][k] - x[j][k]) ** 2
            if sum ** 0.5 % 1 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 4

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k])**2
            if int(dist**0.5)**2 == dist:
                cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k])**2
            if int(d**0.5)**2 == d:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for i in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    n,d = map(int,input().split())
    x = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            dis = 0
            for k in range(d):
                dis += (x[i][k]-x[j][k])**2
            if int(dis**0.5)**2 == dis:
                cnt += 1
    print(cnt)
solve()

=======
Suggestion 8

def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])**2
    return d**0.5

=======
Suggestion 9

def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])*(x[i]-y[i])
    return int(d**0.5)

n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j])**2 == distance(x[i],x[j])*distance(x[i],x[j]):
            ans += 1
print(ans)

=======
Suggestion 10

def calc_distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if calc_distance(x[i], x[j]).is_integer():
            cnt += 1

print(cnt)
