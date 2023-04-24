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
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (y[i]-y[j])*(x[i]-x[k]) == (y[i]-y[k])*(x[i]-x[j]):
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
                if x[i] == x[j] and x[j] == x[k]:
                    print("Yes")
                    return
                elif y[i] == y[j] and y[j] == y[k]:
                    print("Yes")
                    return
                elif (y[j] - y[i]) * (x[k] - x[i]) == (y[k] - y[i]) * (x[j] - x[i]):
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 3

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    print('Yes')
                    return
    print('No')
main()

=======
Suggestion 4

def check(a, b, c):
    if a[0] == b[0] == c[0]:
        return True
    if a[1] == b[1] == c[1]:
        return True
    if a[0] == b[0] or a[0] == c[0] or b[0] == c[0]:
        return False
    if a[1] == b[1] or a[1] == c[1] or b[1] == c[1]:
        return False
    if (a[0] - b[0]) * (a[1] - c[1]) == (a[0] - c[0]) * (a[1] - b[1]):
        return True
    return False

n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

ans = False
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check(xy[i], xy[j], xy[k]):
                ans = True
print("Yes" if ans else "No")

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (xy[j][1]-xy[i][1])*(xy[k][0]-xy[i][0]) == (xy[k][1]-xy[i][1])*(xy[j][0]-xy[i][0]):
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x1 - x2) * (y3 - y2) == (x3 - x2) * (y1 - y2):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 8

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (points[i][0]-points[j][0])*(points[j][1]-points[k][1]) == (points[i][1]-points[j][1])*(points[j][0]-points[k][0]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 9

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    #print(p)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (p[j][0]-p[i][0])*(p[k][1]-p[i][1]) == (p[k][0]-p[i][0])*(p[j][1]-p[i][1]):
                    print('Yes')
                    exit()
    print('No')

=======
Suggestion 10

def check_line(x1,y1,x2,y2,x3,y3):
    #print("check_line")
    #print(x1,y1,x2,y2,x3,y3)
    #print((y2-y1)*(x3-x2))
    #print((y3-y2)*(x2-x1))
    if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
        return True
    else:
        return False

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i],y[i] = map(int,input().split())

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if check_line(x[i],y[i],x[j],y[j],x[k],y[k]):
                print("Yes")
                exit()
print("No")
