Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calDistance(x,y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return sum**0.5

=======
Suggestion 2

def get_distance(x,y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    return int(sum**0.5)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = sum(map(lambda x: (x[0]-x[1])**2, zip(X[i], X[j])))**0.5
            if dist.is_integer():
                cnt += 1
    print(cnt)

=======
Suggestion 4

def is_integer(x):
    if x % 1 == 0:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k]-X[j][k])**2
            if d**0.5 % 1 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    # N = 3
    # D = 2
    # X = [[1, 2], [5, 5], [-2, 8]]

    # N = 3
    # D = 4
    # X = [[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]]

    # N = 5
    # D = 1
    # X = [[1], [2], [3], [4], [5]]

    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if (d ** 0.5).is_integer():
                cnt += 1
    print(cnt)

=======
Suggestion 7

def distance(x, y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i])**2
    return d**0.5

=======
Suggestion 8

def distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i]) ** 2
    return sum ** 0.5

=======
Suggestion 9

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
