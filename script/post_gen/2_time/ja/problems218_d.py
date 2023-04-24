Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                for l in range(k+1, N):
                    if X[i] <= X[k] and X[k] < X[j] and X[j] < X[l] and Y[k] <= Y[i] and Y[i] < Y[l] and Y[l] < Y[j]:
                        ans += 1
    print(ans)

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
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                if x[i] == x[j] and y[i] == y[k]:
                    for l in range(k+1,n):
                        if x[i] == x[l] and y[j] == y[l]:
                            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i], y[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if x[i] == x[j] and y[j] == y[k] and x[k] == x[i]:
                    ans += 1
    print(ans//2)

=======
Suggestion 4

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    xy.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            a = xy[j][1] - xy[i][1]
            b = xy[j][0] - xy[i][0]
            p = xy[i][0] - a
            q = xy[i][1] + b
            r = xy[j][0] - a
            s = xy[j][1] + b
            if [p, q] in xy and [r, s] in xy:
                ans += 1
    print(ans//2)

=======
Suggestion 5

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    if x[i] == x[j] and x[k] == x[l] and y[i] == y[k] and y[j] == y[l]:
                        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    points = [list(map(int, input().split())) for i in range(N)]
    points.sort()

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if points[i][0] == points[j][0] and points[j][0] == points[k][0]:
                    continue
                if points[i][1] == points[j][1] and points[j][1] == points[k][1]:
                    continue

                x = points[j][0] - points[i][0]
                y = points[k][1] - points[i][1]
                if points[i][0] + y >= points[k][0] and points[i][1] + x >= points[j][1]:
                    ans += 1

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    point = [list(map(int,input().split())) for _ in range(N)]
    point.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            x = point[j][0] - point[i][0]
            y = point[j][1] - point[i][1]
            for k in range(j+1,N):
                if point[k][0] == point[i][0] + y and point[k][1] == point[i][1] - x:
                    for l in range(k+1,N):
                        if point[l][0] == point[j][0] + y and point[l][1] == point[j][1] - x:
                            ans += 1
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: x[0])
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            # ここで、A[i][0] <= A[j][0] と仮定する
            # A[i][0] = A[j][0] なら、A[i][1] < A[j][1] と仮定する
            # このとき、A[i][0] = A[j][0] かつ A[i][1] = A[j][1] はありえない
            # なぜなら、点の座標は全て整数であるから
            # したがって、A[i][0] = A[j][0] かつ A[i][1] = A[j][1] はありえない
            # したがって、A[i][0] = A[j][0] なら、A[i][1] < A[j][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] かつ A[i][1] + (A[j][0] - A[i][0]) == A[j][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] かつ A[j][1] - (A[j][0] - A[i][0]) == A[i][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] かつ A[i][0] <= A[j][1] - (A[j][0] - A[i][0]) <= A[j][0] である

=======
Suggestion 9

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    #print(points)
    
    #x座標の差が同じものを探す
    x_diff = []
    for i in range(N):
        for j in range(i+1, N):
            x_diff.append(points[j][0] - points[i][0])
    x_diff.sort()
    #print(x_diff)
    
    #y座標の差が同じものを探す
    y_diff = []
    for i in range(N):
        for j in range(i+1, N):
            y_diff.append(points[j][1] - points[i][1])
    y_diff.sort()
    #print(y_diff)
    
    #x座標の差が同じものを探す
    x_diff = []
    for i in range(N):
        for j in range(i+1, N):
            x_diff.append(points[j][0] - points[i][0])
    x_diff.sort()
    #print(x_diff)
    
    #x座標の差が同じもののy座標の差が同じものを探す
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                for l in range(k+1, N):
                    if points[i][0] < points[k][0] and points[k][0] < points[j][0] and points[i][1] < points[l][1] and points[l][1] < points[j][1]:
                        count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    points.sort()
    #print(points)

    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            #print("i = {}, j = {}".format(i, j))
            #print("points[i] = {}, points[j] = {}".format(points[i], points[j]))
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            #print("points[i][0] = {}, points[j][0] = {}, points[i][1] = {}, points[j][1] = {}".format(points[i][0], points[j][0], points[i][1], points[j][1]))
            if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                #print("points[i][0], points[j][1] = {}, points[j][0], points[i][1] = {}".format((points[i][0], points[j][1]), (points[j][0], points[i][1])))
                ans += 1
    print(ans)
