Synthesizing 10/10 solutions

=======
Suggestion 1

def isLine(points):
    if len(points) < 3:
        return False
    if len(points) == 3:
        return True
    x1, y1 = points[0]
    x2, y2 = points[1]
    if x1 == x2:
        k = 'x'
    else:
        k = (y2 - y1) / (x2 - x1)
    for i in range(2, len(points)):
        x, y = points[i]
        if k != 'x' and k != (y - y1) / (x - x1):
            return False
        elif k == 'x' and x != x1:
            return False
    return True

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            dx1 = x[j] - x[i]
            dy1 = y[j] - y[i]
            dx2 = x[k] - x[i]
            dy2 = y[k] - y[i]
            if dx1 * dy2 == dx2 * dy1:
                print('Yes')
                exit()

print('No')

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    else:
        return (y2 - y1) / (x2 - x1)

=======
Suggestion 5

def solve():
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
                if (x[i] - x[j]) * (y[j] - y[k]) == (x[j] - x[k]) * (y[i] - y[j]):
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 6

def judge(points):
    for i in xrange(0, len(points)-2):
        for j in xrange(i+1, len(points)-1):
            for k in xrange(j+1, len(points)):
                if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == \
                   (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                    return True
    return False

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(input().split())
    points.sort()
    #print(points)
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (int(points[i][0])-int(points[j][0]))*(int(points[j][1])-int(points[k][1])) == (int(points[i][1])-int(points[j][1]))*(int(points[j][0])-int(points[k][0])):
                    print('Yes')
                    return
    print('No')
    return

main()

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 9

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
ans = "No"
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1 = x[i] - x[j]
            y1 = y[i] - y[j]
            x2 = x[j] - x[k]
            y2 = y[j] - y[k]
            if x1*y2 == x2*y1:
                ans = "Yes"
                break
print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    x_y = []
    for i in range(n):
        x_y.append(list(map(int,input().split())))

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (x_y[i][0]-x_y[j][0])*(x_y[i][1]-x_y[k][1]) == (x_y[i][0]-x_y[k][0])*(x_y[i][1]-x_y[j][1]):
                    print("Yes")
                    return
    print("No")
