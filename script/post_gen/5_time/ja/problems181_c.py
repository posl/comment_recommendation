Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 2

def main():
    # N = int(input())
    # X = [0 for _ in range(N)]
    # Y = [0 for _ in range(N)]
    # for i in range(N):
    #     X[i],Y[i] = map(int,input().split())
    #     # print(X[i],Y[i])
    # for i in range(N):
    #     for j in range(i+1,N):
    #         for k in range(j+1,N):
    #             if (Y[i]-Y[j])*(X[i]-X[k]) == (Y[i]-Y[k])*(X[i]-X[j]):
    #                 print("Yes")
    #                 return
    # print("No")
    N = int(input())
    X = [0 for _ in range(N)]
    Y = [0 for _ in range(N)]
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (Y[i]-Y[j])*(X[i]-X[k]) == (Y[i]-Y[k])*(X[i]-X[j]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 3

def solve():
    n = int(input())
    points = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                x3,y3 = points[k]
                if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 4

def main():
    print("Hello World!")
    return

=======
Suggestion 5

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = "No"
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1 = xy[i][0]
                y1 = xy[i][1]
                x2 = xy[j][0]
                y2 = xy[j][1]
                x3 = xy[k][0]
                y3 = xy[k][1]
                if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
                    ans = "Yes"
    print(ans)

=======
Suggestion 6

def main():
    # input
    N = int(input())
    XYs = []
    for _ in range(N):
        XYs.append(list(map(int, input().split())))
    # compute
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = XYs[i]
                x2, y2 = XYs[j]
                x3, y3 = XYs[k]
                if (y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1):
                    ans = 'Yes'
    # output
    print(ans)

=======
Suggestion 7

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

=======
Suggestion 8

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 9

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if x1 == x2 and x1 == x3:
                    print('Yes')
                    return
                if x1 == x2:
                    continue
                if x2 == x3:
                    continue
                if x1 == x3:
                    continue
                if y1 == y2 and y1 == y3:
                    print('Yes')
                    return
                if y1 == y2:
                    continue
                if y2 == y3:
                    continue
                if y1 == y3:
                    continue
                if (x1-x2)/(y1-y2) == (x1-x3)/(y1-y3):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 10

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append([int(x) for x in input().split()])
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print('Yes')
                    return
    print('No')
    return
