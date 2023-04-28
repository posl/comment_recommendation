Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if dist**0.5 == int(dist**0.5):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            distance = 0
            for k in range(D):
                distance += (X[i][k] - X[j][k])**2
            if int(distance**0.5)**2 == distance:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = 0
            for k in range(d):
                distance += (points[i][k] - points[j][k])**2
            if (distance**0.5).is_integer():
                count += 1
    print(count)

=======
Suggestion 4

def get_input():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    return N, D, X

=======
Suggestion 5

def distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i]) ** 2
    return sum ** 0.5

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(x[i], x[j]).is_integer():
            ans += 1
print(ans)

=======
Suggestion 6

def get_input():
    n, d = map(int, input().split())
    xs = [list(map(int, input().split())) for _ in range(n)]
    return n, d, xs

=======
Suggestion 7

def main():
    import sys
    import math
    n, d = map(int, sys.stdin.readline().split())
    x = []
    for i in range(n):
        x.append(list(map(int, sys.stdin.readline().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k]) ** 2
            if math.sqrt(dist).is_integer():
                ans += 1
    print(ans)

=======
Suggestion 8

def get_input():
    n,d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    return n,d,x

=======
Suggestion 9

def distance(p1, p2):
    return sum([(a-b)**2 for a, b in zip(p1, p2)])**0.5

N, D = [int(x) for x in input().split()]
points = [[int(x) for x in input().split()] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(i+1, N):
        if distance(points[i], points[j]).is_integer():
            count += 1
print(count)

=======
Suggestion 10

def is_integer_distance(x, y):
  distance = 0
  for i in range(len(x)):
    distance += (x[i] - y[i]) ** 2
  if distance ** (1/2) % 1 == 0:
    return True
  else:
    return False

n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
count = 0

for i in range(n):
  for j in range(i+1, n):
    if is_integer_distance(x[i], x[j]):
      count += 1
print(count)
