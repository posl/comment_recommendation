Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if x[i] == x[j] and x[j] == x[k]:
                    print("Yes")
                    return
                elif y[i] == y[j] and y[j] == y[k]:
                    print("Yes")
                    return
                elif (y[i]-y[j])*(x[i]-x[k]) == (y[i]-y[k])*(x[i]-x[j]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if x[i] == x[j] == x[k] or y[i] == y[j] == y[k]:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 3

def isCollinear(x1, y1, x2, y2, x3, y3):
    return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if isCollinear(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit(0)
print('No')

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2):
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 5

def check_line(a,b,c):
    if (a[0] == b[0] and b[0] == c[0]) or (a[1] == b[1] and b[1] == c[1]):
        return True
    elif (a[1] - b[1]) / (a[0] - b[0]) == (b[1] - c[1]) / (b[0] - c[0]):
        return True
    else:
        return False

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if check_line(points[i],points[j],points[k]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 6

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            for k in range(j+1, n):
                x3, y3 = points[k]
                if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 7

def check_line(x1,y1,x2,y2,x3,y3):
    if (x1-x2)*(y3-y2) == (y1-y2)*(x3-x2):
        return True
    else:
        return False

=======
Suggestion 8

def check_if_on_line(x1,y1,x2,y2,x3,y3):
    if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
        return True
    else:
        return False

=======
Suggestion 9

def checkLine(points):
    if len(points) < 3:
        return False
    if points[0][0] == points[1][0] == points[2][0]:
        return True
    if points[0][1] == points[1][1] == points[2][1]:
        return True
    if points[0][0] == points[1][0] and points[0][0] == points[2][0]:
        return True
    if points[0][1] == points[1][1] and points[0][1] == points[2][1]:
        return True
    if points[0][0] == points[1][0]:
        if points[0][0] == points[2][0]:
            return True
        return False
    if points[0][1] == points[1][1]:
        if points[0][1] == points[2][1]:
            return True
        return False
    if points[0][1] - points[1][1] == points[0][0] - points[1][0]:
        if points[0][1] - points[2][1] == points[0][0] - points[2][0]:
            return True
        return False
    return False

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
points.sort()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if checkLine([points[i], points[j], points[k]]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 10

def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    result = "No"
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (x[j] - x[i]) * (y[k] - y[i]) == (x[k] - x[i]) * (y[j] - y[i]):
                    result = "Yes"
                    break
            else:
                continue
            break
        else:
            continue
        break
    print(result)
