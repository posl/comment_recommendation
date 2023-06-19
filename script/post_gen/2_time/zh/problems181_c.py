Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # TODO
    pass

=======
Suggestion 2

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def check_inline (x1, y1, x2, y2, x3, y3):
    if (x1-x2)*(y2-y3) == (x2-x3)*(y1-y2):
        return True
    else:
        return False

=======
Suggestion 5

def line(x1,y1,x2,y2,x3,y3):
    if x1==x2==x3:
        return True
    elif y1==y2==y3:
        return True
    elif x1==x2 and x2==x3:
        return True
    elif y1==y2 and y2==y3:
        return True
    elif (y1-y2)/(x1-x2)==(y2-y3)/(x2-x3):
        return True
    else:
        return False

=======
Suggestion 6

def is_line(x1, y1, x2, y2, x3, y3):
    if x1 == x2 == x3:
        return True
    elif y1 == y2 == y3:
        return True
    elif x1 == x2 and x1 == x3:
        return True
    elif y1 == y2 and y1 == y3:
        return True
    elif (x1-x2) * (y1-y3) == (x1-x3) * (y1-y2):
        return True
    else:
        return False

=======
Suggestion 7

def isLine(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        if x2 == x3:
            return True
        else:
            return False
    elif x2 == x3:
        return False
    elif y1 == y2:
        if y2 == y3:
            return True
        else:
            return False
    elif y2 == y3:
        return False
    elif (y1 - y2) / (x1 - x2) == (y2 - y3) / (x2 - x3):
        return True
    else:
        return False

=======
Suggestion 8

def check_line(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and x2 == x3:
        return True
    elif y1 == y2 and y2 == y3:
        return True
    else:
        return False

=======
Suggestion 9

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
                if x[i] == x[j]:
                    if x[i] == x[k]:
                        print('Yes')
                        return
                elif y[i] == y[j]:
                    if y[i] == y[k]:
                        print('Yes')
                        return
                elif x[i] != x[j]:
                    if (y[i] - y[j])/(x[i] - x[j]) == (y[i] - y[k])/(x[i] - x[k]):
                        print('Yes')
                        return
    print('No')
    return

=======
Suggestion 10

def isLine(x1, y1, x2, y2, x3, y3):
    if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
        return True
    else:
        return False

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

res = "No"
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if isLine(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                res = "Yes"

print(res)
