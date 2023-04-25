Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
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
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if (dist ** 0.5) % 1 == 0:
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
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k])**2
            if (dist**0.5).is_integer():
                count += 1
    print(count)

=======
Suggestion 5

def get_input():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    return n, d, x

=======
Suggestion 6

def main():
    # Get input here
    n, d = map(int, input().split())
    coordinates = []
    for _ in range(n):
        coordinates.append(list(map(int, input().split())))

    # Calculate result here
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            distance = 0
            for k in range(d):
                distance += (coordinates[i][k] - coordinates[j][k]) ** 2
            if (distance ** 0.5).is_integer():
                result += 1

    # Print result here
    print(result)

=======
Suggestion 7

def main():
    from collections import defaultdict
    import itertools
    from math import sqrt
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i, j in itertools.combinations(range(n), 2):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        if sqrt(dist).is_integer():
            cnt += 1
    print(cnt)

=======
Suggestion 8

def euclideanDistance(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

=======
Suggestion 9

def get_distance(x,y):
    square_sum = 0
    for i in range(len(x)):
        square_sum += (x[i] - y[i])**2
    return int(square_sum**0.5)

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i+1,n):
        if get_distance(x[i], x[j])**2 == get_distance(x[i], x[j]):
            count += 1
print(count)

=======
Suggestion 10

def get_int():
    return int(input().strip())
