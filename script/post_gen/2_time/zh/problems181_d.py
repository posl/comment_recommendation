Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 3

def get_line(x1,y1,x2,y2):
    if x1==x2:
        return 'x='+str(x1)
    elif y1==y2:
        return 'y='+str(y1)
    else:
        k=(y1-y2)/(x1-x2)
        b=y1-k*x1
        return 'y='+str(k)+'x+'+str(b)

=======
Suggestion 4

def solve():
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
                if x1 == x2 and x2 == x3:
                    print('Yes')
                    return
                elif x1 == x2 or x2 == x3:
                    continue
                else:
                    if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
                        print('Yes')
                        return
    print('No')
solve()

=======
Suggestion 5

def isLine(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and x1 == x3:
        return True
    elif y1 == y2 and y1 == y3:
        return True
    elif (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
        return True
    else:
        return False

=======
Suggestion 6

def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return float('inf')
    else:
        return (y2 - y1) / (x2 - x1)

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append((x,y))
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if points[i][0] == points[j][0]:
                    if points[i][0] == points[k][0]:
                        print('Yes')
                        return
                elif points[i][1] == points[j][1]:
                    if points[i][1] == points[k][1]:
                        print('Yes')
                        return
                else:
                    if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                        print('Yes')
                        return
    print('No')
main()

=======
Suggestion 8

def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "inf"
    else:
        return (y2-y1)/(x2-x1)

=======
Suggestion 9

def is_same_line(p1, p2, p3):
    if p1[0] == p2[0] and p2[0] == p3[0]:
        return True
    if p1[1] == p2[1] and p2[1] == p3[1]:
        return True
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return False
    if p1[0] == p3[0] or p1[1] == p3[1]:
        return False
    if p2[0] == p3[0] or p2[1] == p3[1]:
        return False
    if (p1[0] - p2[0]) * (p1[1] - p3[1]) == (p1[0] - p3[0]) * (p1[1] - p2[1]):
        return True
    else:
        return False

=======
Suggestion 10

def find(a, b):
    if a[0] == b[0]:
        return 0
    elif a[1] == b[1]:
        return 1
    else:
        return 2
