Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]
                if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                    continue
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1 = xy[i][0] - xy[k][0]
                y1 = xy[i][1] - xy[k][1]
                x2 = xy[j][0] - xy[k][0]
                y2 = xy[j][1] - xy[k][1]
                if x1*y2 - x2*y1 != 0:
                    ans += 1
    print(ans)

=======
Suggestion 3

def calc_area(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2

N = int(input())

points = []
for i in range(N):
    points.append(list(map(int, input().split())))

=======
Suggestion 4

def main():
    N = int(input())
    XY = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]
                if x1 == x2:
                    if x2 == x3:
                        continue
                    else:
                        ans += 1
                        continue
                elif x2 == x3:
                    if x3 == x1:
                        continue
                    else:
                        ans += 1
                        continue
                elif x3 == x1:
                    if x1 == x2:
                        continue
                    else:
                        ans += 1
                        continue
                if y1 == y2:
                    if y2 == y3:
                        continue
                    else:
                        ans += 1
                        continue
                elif y2 == y3:
                    if y3 == y1:
                        continue
                    else:
                        ans += 1
                        continue
                elif y3 == y1:
                    if y1 == y2:
                        continue
                    else:
                        ans += 1
                        continue
                if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    continue
                else:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    points = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[k][0]
                y3 = points[k][1]
                if (x1-x3)*(y2-y3) != (x2-x3)*(y1-y3):
                    count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    xy = []
    for i in range(n):
        x,y = map(int,input().split())
        xy.append((x,y))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1,y1 = xy[i]
                x2,y2 = xy[j]
                x3,y3 = xy[k]
                x1 -= x3
                x2 -= x3
                y1 -= y3
                y2 -= y3
                if x1*y2 != x2*y1:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    points = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                    continue
                ans += 1
    print(ans)

=======
Suggestion 8

def area(x1,y1,x2,y2,x3,y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2

N=int(input())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

ans=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if area(X[i],Y[i],X[j],Y[j],X[k],Y[k])>0:
                ans+=1
print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[k][0]
                y3 = points[k][1]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    continue
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    import sys
    readline = sys.stdin.buffer.readline
    N = int(readline())
    XY = [list(map(int,readline().split())) for _ in range(N)]
    XY.sort(key = lambda x:x[0])
    XY.sort(key = lambda x:x[1])
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                a = XY[i]
                b = XY[j]
                c = XY[k]
                if (b[0]-a[0])*(c[1]-a[1]) != (c[0]-a[0])*(b[1]-a[1]):
                    ans += 1
    print(ans)
