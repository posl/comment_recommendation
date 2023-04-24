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
                dist += (X[i][d] - X[j][d])**2
            if (dist**0.5).is_integer():
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
                dist += (X[i][k]-X[j][k])**2
            if (dist**0.5).is_integer():
                ans += 1
    print(ans)

main()

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
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
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k])**2
            if (d**0.5).is_integer():
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,d = map(int,input().split())
    x = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if dist**0.5 == int(dist**0.5):
                ans += 1
    print(ans)

=======
Suggestion 7

def distance(a, b):
    result = 0
    for i in range(len(a)):
        result += (a[i] - b[i]) ** 2
    return result ** 0.5

=======
Suggestion 8

def get_distance(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i] - b[i]) ** 2
    return int(distance ** 0.5)

=======
Suggestion 9

def calcDistance(x,y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i])**2
    return sum**0.5

=======
Suggestion 10

def distance(x1, x2):
    return ((x1-x2)**2)**(1/2)
