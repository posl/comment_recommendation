Synthesizing 10/10 solutions

=======
Suggestion 1

def get_distance(d, x1, x2):
    distance = 0
    for i in range(d):
        distance += (x1[i] - x2[i]) ** 2
    return int(distance ** 0.5)

=======
Suggestion 2

def distance(x, y):
    return sum((a-b)**2 for a, b in zip(x, y))**0.5

=======
Suggestion 3

def get_distance(x, y):
    distance = 0
    for i in range(len(x)):
        distance += (x[i] - y[i]) ** 2
    return distance

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        distance = get_distance(X[i], X[j])
        if (distance ** 0.5).is_integer():
            count += 1
print(count)

=======
Suggestion 4

def get_distance(x, y):
    result = 0
    for i in range(len(x)):
        result += (x[i]-y[i])**2
    return result**0.5

=======
Suggestion 5

def calcDist(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i])**2
    return dist**0.5

=======
Suggestion 6

def distance(x, y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    return d ** 0.5

=======
Suggestion 7

def getDistance(p1, p2):
    D = len(p1)
    sum = 0
    for i in range(D):
        sum += (p1[i] - p2[i]) ** 2
    return sum ** 0.5

N, D = map(int, input().split())

points = []
for i in range(N):
    points.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(i+1, N):
        if getDistance(points[i], points[j]).is_integer():
            count += 1

print(count)

=======
Suggestion 8

def get_distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def get_distance(x, y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    return d ** 0.5
