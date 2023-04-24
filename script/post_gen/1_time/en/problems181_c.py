Synthesizing 10/10 solutions

=======
Suggestion 1

def line_check(a, b, c):
    if a[0] == b[0] == c[0]:
        return True
    elif a[1] == b[1] == c[1]:
        return True
    elif (a[0] - b[0]) * (a[1] - c[1]) == (a[1] - b[1]) * (a[0] - c[0]):
        return True
    else:
        return False

=======
Suggestion 2

def main():
    n = int(input())
    xy = []

    for i in range(n):
        xy.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (xy[i][0] - xy[j][0]) * (xy[j][1] - xy[k][1]) == (xy[j][0] - xy[k][0]) * (xy[i][1] - xy[j][1]):
                    print("Yes")
                    return

    print("No")

=======
Suggestion 3

def check_line(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        return x1 == x3
    elif x2 == x3:
        return x1 == x2
    else:
        return (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if check_line(x1, y1, x2, y2, x3, y3):
                print("Yes")
                exit()
print("No")

=======
Suggestion 4

def check_line(x1, y1, x2, y2, x3, y3):
    if (x1 == x2 and x1 == x3):
        return True
    if (y1 == y2 and y1 == y3):
        return True
    if ((x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2)):
        return True
    return False

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

flag = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check_line(s[i][0], s[i][1], s[j][0], s[j][1], s[k][0], s[k][1]):
                flag = True
                break
        if (flag):
            break
    if (flag):
        break

=======
Suggestion 5

def calc_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'inf'
    else:
        return (y2 - y1) / (x2 - x1)

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if calc_slope(x1, y1, x2, y2) == calc_slope(x2, y2, x3, y3):
                print('Yes')
                exit()

print('No')

=======
Suggestion 6

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int,input().split())))
    points.sort()
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (points[i][0]-points[j][0])*(points[j][1]-points[k][1]) == (points[i][1]-points[j][1])*(points[j][0]-points[k][0]):
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 7

def main():
    # Get the number of points
    n = int(input())

    # Get the points
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Find the line equation of all possible lines
    # y = ax + b
    lines = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # If the two points are on the same vertical line
            if x1 == x2:
                a = float('inf')
                b = x1
            # If the two points are on the same horizontal line
            elif y1 == y2:
                a = 0
                b = y1
            # If the two points are on the same diagonal line
            elif abs(x1 - x2) == abs(y1 - y2):
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1
            # If the two points are on the same line
            else:
                continue

            # Add the line equation to the list
            lines.append((a, b))

    # Check if there are 3 points on the same line
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            for k in range(j + 1, len(lines)):
                if lines[i] == lines[j] and lines[j] == lines[k]:
                    print('Yes')
                    exit()

    print('No')

=======
Suggestion 8

def slope(x1,y1,x2,y2):
    if x1 == x2:
        return float('inf')
    return (y2-y1)/(x2-x1)

=======
Suggestion 9

def get_input():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    return n, points

=======
Suggestion 10

def check_if_on_line(x1,y1,x2,y2,x3,y3):
    return (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)

N = int(input())
points = [list(map(int,input().split())) for i in range(N)]
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if check_if_on_line(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]):
                print('Yes')
                exit()
print('No')
