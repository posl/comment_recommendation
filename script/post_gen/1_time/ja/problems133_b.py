Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            dist = 0
            for d in range(D):
                dist += (X[i][d] - X[j][d]) ** 2
            dist = dist ** 0.5
            if dist == int(dist):
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
            sum = 0
            for k in range(D):
                sum += (X[i][k] - X[j][k]) ** 2
            if int(sum ** 0.5) == sum ** 0.5:
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
            dist = 0
            for d in range(D):
                dist += (X[i][d] - X[j][d]) ** 2
            dist = dist ** 0.5
            if dist.is_integer():
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            dis = 0
            for k in range(D):
                dis += (X[i][k] - X[j][k]) ** 2
            if dis ** 0.5 == int(dis ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            dist2 = 0
            for k in range(D):
                dist2 += (X[i][k] - X[j][k]) ** 2
            if dist2 ** 0.5 == int(dist2 ** 0.5):
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k]-x[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
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
Suggestion 8

def main():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            distance = 0
            for k in range(D):
                distance += (X[i][k]-X[j][k])**2
            if distance**0.5 == int(distance**0.5):
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N, D = map(int,input().split())
    X = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 == int(d ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, d = map(int, input().split())
    x = [[int(i) for i in input().split()] for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if dist**0.5 == int(dist**0.5):
                ans += 1
    print(ans)
