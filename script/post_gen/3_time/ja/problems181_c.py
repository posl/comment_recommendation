Synthesizing 10/10 solutions

=======
Suggestion 1

def check(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if check(x1, y1, x2, y2, x3, y3):
                print('Yes')
                exit()
print('No')

=======
Suggestion 2

def check(x1, y1, x2, y2, x3, y3):
    return (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1)

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if check(x[i], y[i], x[j], y[j], x[k], y[k]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if x[i] == x[j] == x[k]:
                    print("Yes")
                    return
                elif x[i] == x[j] or x[i] == x[k] or x[j] == x[k]:
                    continue
                else:
                    if (y[i] - y[j]) / (x[i] - x[j]) == (y[i] - y[k]) / (x[i] - x[k]):
                        print("Yes")
                        return
    print("No")
main()

=======
Suggestion 5

def calc(x1, y1, x2, y2, x3, y3):
    if x1 == x2 == x3:
        return True
    elif y1 == y2 == y3:
        return True
    elif (x1 - x2) * (y1 - y3) == (x1 - x3) * (y1 - y2):
        return True
    else:
        return False

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if calc(x1, y1, x2, y2, x3, y3):
                print("Yes")
                exit()

print("No")

=======
Suggestion 6

def main():
    n = int(input())
    p = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (p[j][0] - p[i][0]) * (p[k][1] - p[i][1]) == (p[j][1] - p[i][1]) * (p[k][0] - p[i][0]):
                    print('Yes')
                    exit()
    print('No')

=======
Suggestion 7

def check(a,b,c):
    if(a[0] == b[0] and b[0] == c[0]):
        return True
    elif(a[1] == b[1] and b[1] == c[1]):
        return True
    elif(a[0] == b[0] and b[0] != c[0]):
        return False
    elif(a[1] == b[1] and b[1] != c[1]):
        return False
    else:
        if((a[1] - b[1])/(a[0] - b[0]) == (b[1] - c[1])/(b[0] - c[0])):
            return True
        else:
            return False

N = int(input())
xy = [list(map(int,input().split())) for i in range(N)]

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if(check(xy[i],xy[j],xy[k])):
                print('Yes')
                exit()
print('No')

=======
Suggestion 8

def chk(a,b,c):
    x1 = a[0]
    x2 = b[0]
    x3 = c[0]
    y1 = a[1]
    y2 = b[1]
    y3 = c[1]
    if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
        return True
    else:
        return False

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if chk(xy[i],xy[j],xy[k]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 9

def solve():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 10

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
