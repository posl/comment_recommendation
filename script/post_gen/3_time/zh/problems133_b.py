Synthesizing 10/10 solutions

=======
Suggestion 1

def get_distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5

=======
Suggestion 2

def dist(x,y):
    sum=0
    for i in range(len(x)):
        sum+=(x[i]-y[i])**2
    return sum**0.5

=======
Suggestion 3

def calc_distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return int(sum**0.5)

=======
Suggestion 4

def get_input():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    return n, d, x

=======
Suggestion 5

def distance(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return d ** 0.5

N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(i+1, N):
        if distance(X[i], X[j]).is_integer():
            count += 1

print(count)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum = 0
            for k in range(d):
                sum += (x[i][k] - x[j][k]) ** 2
            if sum ** 0.5 == int(sum ** 0.5):
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, d = [int(i) for i in input().split()]
    x = [[int(i) for i in input().split()] for j in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            dis = 0
            for k in range(d):
                dis += (x[i][k] - x[j][k]) ** 2
            if int(dis ** 0.5) ** 2 == dis:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = sum((x-y)**2 for x, y in zip(X[i], X[j]))
            if int(dist**0.5)**2 == dist:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 == int(d ** 0.5):
                count += 1

    print(count)
