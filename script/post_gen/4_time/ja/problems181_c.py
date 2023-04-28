Synthesizing 10/10 solutions

=======
Suggestion 1

def check(x1, y1, x2, y2, x3, y3):
    return (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2)

n = int(input())
x, y = [], []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check(x[i], y[i], x[j], y[j], x[k], y[k]):
                print("Yes")
                exit()

print("No")

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j]):
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 3

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 4

def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 5

def check(x1, y1, x2, y2, x3, y3):
    if x1 - x2 == 0:
        if x1 - x3 == 0:
            return True
        else:
            return False
    else:
        if x1 - x3 == 0:
            return False
        else:
            if (y1 - y2) / (x1 - x2) == (y1 - y3) / (x1 - x3):
                return True
            else:
                return False

N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if check(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()

print('No')

=======
Suggestion 6

def check_on_line(x1, y1, x2, y2, x3, y3):
    return (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)

N = int(input())
points = []
for i in range(N):
    x,y = map(int, input().split())
    points.append((x,y))

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check_on_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')

=======
Suggestion 7

def check(x1,y1,x2,y2,x3,y3):
    if x1==x2 and x1==x3:
        return True
    if x1==x2:
        return False
    if x1==x3:
        return False
    if x2==x3:
        return False
    if y1==y2 and y1==y3:
        return True
    if y1==y2:
        return False
    if y1==y3:
        return False
    if y2==y3:
        return False
    if (y2-y1)*(x3-x1)==(y3-y1)*(x2-x1):
        return True
    return False

N = int(input())
xy = []
for i in range(N):
    x,y = map(int,input().split())
    xy.append((x,y))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(xy[i][0],xy[i][1],xy[j][0],xy[j][1],xy[k][0],xy[k][1]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 8

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    if N < 3:
        print("No")
        return
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if points[i][0] == points[j][0] and points[i][0] == points[k][0]:
                    print("Yes")
                    return
                elif points[i][1] == points[j][1] and points[i][1] == points[k][1]:
                    print("Yes")
                    return
                elif (points[i][0] - points[j][0]) * (points[j][1] - points[k][1]) == (points[j][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 9

def check():
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if ((x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j])):
                    return True
    return False

N = int(input())
x = [0] * N
y = [0] * N

for i in range(0, N):
    x[i], y[i] = map(int, input().split())

=======
Suggestion 10

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x
