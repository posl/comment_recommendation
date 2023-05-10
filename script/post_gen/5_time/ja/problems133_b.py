Synthesizing 10/10 solutions

=======
Suggestion 1

def euclidean_distance(x, y):
    return sum([(x_i - y_i)**2 for x_i, y_i in zip(x, y)])**0.5

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        if euclidean_distance(x[i], x[j]).is_integer():
            ans += 1
print(ans)

=======
Suggestion 2

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            distance = 0
            for k in range(D):
                distance += (X[i][k] - X[j][k]) ** 2
            if int(distance ** 0.5) ** 2 == distance:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum = 0
            for k in range(D):
                sum += (X[i][k] - X[j][k]) ** 2
            if (sum ** 0.5).is_integer():
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dis = 0
            for k in range(d):
                dis += (x[i][k] - x[j][k]) ** 2
            if (dis ** 0.5).is_integer():
                ans += 1
    print(ans)

=======
Suggestion 5

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
            dist = dist ** 0.5
            if dist.is_integer():
                ans += 1
    print(ans)

main()

=======
Suggestion 6

def main():
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
            if d**0.5 == int(d**0.5):
                ans += 1

    print(ans)

main()

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if (int(dist**0.5))**2 == dist:
                ans += 1
    print(ans)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        if dist**0.5 == int(dist**0.5):
            ans += 1

print(ans)

=======
Suggestion 9

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if dist == int(dist ** 0.5) ** 2:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            for l in range(1, 1000):
                if d == l ** 2:
                    ans += 1
                    break
    print(ans)
