Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        if x * x + y * y <= d * d:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        X, Y = map(int, input().split())
        if (X**2 + Y**2)**(1/2) <= D:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x * x + y * y <= D * D:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x**2 + y**2) <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        x, y = map(int, input().split())
        dist = (x**2+y**2)**(1/2)
        if dist <= d:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if (x*x + y*y) <= d*d:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N,D = map(int,input().split())
    count = 0
    for _ in range(N):
        X,Y = map(int,input().split())
        if X**2 + Y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 9

def distance(x1,y1):
    return (x1**2 + y1**2)**0.5

N,D = map(int,input().split())
count = 0
for i in range(N):
    x,y = map(int,input().split())
    if distance(x,y) <= D:
        count += 1
print(count)

=======
Suggestion 10

def main():
    # Get the number of points and the radius
    n, d = map(int, input().split())
    # Initialize the counter
    c = 0
    # Loop through the points
    for i in range(n):
        # Get the point
        x, y = map(int, input().split())
        # Check if the distance is less than or equal to the radius
        if x**2 + y**2 <= d**2:
            # Increment the counter
            c += 1
    # Print the number of points
    print(c)
