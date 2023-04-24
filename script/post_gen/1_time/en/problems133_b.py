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
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 == int(d ** 0.5):
                ans += 1

    print(ans)

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum([(x[i][k] - x[j][k])**2 for k in range(d)])**(1/2)
            if dist.is_integer():
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(n)]
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k])**2
            if dist**0.5 == int(dist**0.5):
                cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n,d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            tmp = 0
            for k in range(d):
                tmp += (x[i][k]-x[j][k])**2
            if tmp**0.5 == int(tmp**0.5):
                ans += 1
    print(ans)

=======
Suggestion 6

def get_input():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    return n, d, x

=======
Suggestion 7

def is_integer(x):
    if x == int(x):
        return True
    else:
        return False

n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k] - x[j][k]) ** 2
        if is_integer(dis ** 0.5):
            ans += 1
print(ans)

=======
Suggestion 8

def main():
    # Get input here
    N, D = [int(x) for x in input().split()]
    points = [[int(x) for x in input().split()] for i in range(N)]

    # Calculate result here
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            sum = 0
            for k in range(D):
                sum += (points[i][k] - points[j][k]) ** 2
            if sum ** 0.5 == int(sum ** 0.5):
                result += 1

    # Print result here
    print(result)

main()

=======
Suggestion 9

def main():
    n, d = map(int, input().split())
    xs = [list(map(int, input().split())) for _ in range(n)]

    def distance(x, y):
        return sum((x_i - y_i) ** 2 for x_i, y_i in zip(x, y)) ** 0.5

    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if distance(xs[i], xs[j]).is_integer():
                result += 1
    print(result)

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
