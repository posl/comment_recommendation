Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
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
            if dist**0.5 == int(dist**0.5):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k])**2
            if d**0.5 == int(d**0.5):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k])**2
            if dist**0.5 == int(dist**0.5):
                ans += 1
    print(ans)

=======
Suggestion 5

def distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5

n, d = map(int, input().split())
points = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(i+1, n):
        if distance(points[i], points[j]) == int(distance(points[i], points[j])):
            count += 1
print(count)

I am trying to create a function that will take a list of numbers and return the sum of the numbers that are divisible by 3 and 5.

=======
Suggestion 6

def distance(x1,x2):
    dist = 0
    for i in range(len(x1)):
        dist += (x1[i] - x2[i])**2
    return dist**(1/2)

=======
Suggestion 7

def distance(a, b):
    return sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** 0.5

=======
Suggestion 8

def get_ints(): return map(int, input().split())

n, d = get_ints()

x = [list(get_ints()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        if int(dist**0.5) == dist**0.5:
            ans += 1

print(ans)

=======
Suggestion 9

def dist( point1, point2 ):
    return sum( (x-y)**2 for x, y in zip(point1, point2) )**0.5
