Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x ** 2 + y ** 2 <= d ** 2:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**0.5 <= D:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x**2 + y**2)**(1/2) <= D:
            count += 1
    print(count)

main()

=======
Suggestion 4

def problem174_b():
    n, d = map(int, input().split())
    count = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if (x**2 + y**2)**(1/2) <= d:
            count += 1
    print(count)

=======
Suggestion 5

def solve():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if X**2 + Y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(N):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)**0.5
        if dist <= D:
            count += 1
    print(count)

=======
Suggestion 7

def distance(x, y):
    return (x**2 + y**2)**0.5

N, D = map(int, input().split())
count = 0
for i in range(N):
    x, y = map(int, input().split())
    if distance(x, y) <= D:
        count += 1
print(count)

=======
Suggestion 8

def distance(x, y):
    return (x**2 + y**2)**(1/2)

N, D = map(int, input().split())

count = 0
for i in range(N):
    x, y = map(int, input().split())
    if distance(x, y) <= D:
        count += 1

print(count)

=======
Suggestion 9

def get_input():
    n, d = map(int, input().split())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    return n, d, points

=======
Suggestion 10

def calc_distance(x, y):
    return (x ** 2 + y ** 2) ** 0.5
