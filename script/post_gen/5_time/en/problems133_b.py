Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 == int(d ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 == int(d ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    X = []
    for _ in range(N):
        X.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                cnt += 1
    print(cnt)

=======
Suggestion 4

def distance(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return d ** 0.5

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(x[i], x[j]).is_integer():
            cnt += 1

print(cnt)

=======
Suggestion 5

def main():
    N,D = map(int,input().split())
    X = []
    for i in range(N):
        x = list(map(int,input().split()))
        X.append(x)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            sum = 0
            for k in range(D):
                sum += (X[i][k] - X[j][k])**2
            if sum**0.5 == int(sum**0.5):
                count += 1
    print(count)
main()

=======
Suggestion 6

def distance(a, b, d):
    total = 0
    for i in range(d):
        total += (a[i] - b[i]) ** 2
    return total ** 0.5

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(x[i], x[j], d).is_integer():
            ans += 1
print(ans)

=======
Suggestion 7

def get_input():
    n,d = [int(x) for x in input().split()]
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    return n,d,points

=======
Suggestion 8

def get_distance(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist ** 0.5

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 10

def solve():
    # implement process
    return 0
