Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j]:
                continue
            for k in range(j+1, n):
                if y[i] == y[k]:
                    continue
                if x[k] == x[j]:
                    continue
                if y[j] == y[k]:
                    continue
                if x[i] == x[k]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 4

def getRectNum(pointList):
    rectNum = 0
    for i in range(len(pointList)):
        for j in range(i+1, len(pointList)):
            if pointList[i][0] < pointList[j][0] and pointList[i][1] < pointList[j][1]:
                if [pointList[i][0], pointList[j][1]] in pointList and [pointList[j][0], pointList[i][1]] in pointList:
                    rectNum += 1
            elif pointList[i][0] > pointList[j][0] and pointList[i][1] > pointList[j][1]:
                if [pointList[i][0], pointList[j][1]] in pointList and [pointList[j][0], pointList[i][1]] in pointList:
                    rectNum += 1
    return rectNum

=======
Suggestion 5

def get_input():
    N = int(input())
    points = []
    for i in range(N):
        points.append(tuple(map(int, input().split())))
    return points

=======
Suggestion 6

def find(a,b):
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] == a[j] and b[i] == b[j]:
                count += 1
    return count

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] != x[j] and y[i] != y[j]:
                if x[i] in x and y[j] in y:
                    count += 1
    print(count)

=======
Suggestion 8

def get_input():
    num = int(raw_input())
    points = []
    for i in range(num):
        points.append(map(int, raw_input().split()))
    return points

=======
Suggestion 9

def get_count_of_rectangles(points):
    # 1. 从所有点中找出位于x轴上的点
    # 2. 从所有点中找出位于y轴上的点
    # 3. 算出每个x轴上的点和y轴上的点的组合
    # 4. 算出每个组合能组成的矩形个数
    # 5. 累加每个组合的矩形个数
    # 6. 返回累加的结果
    count = 0
    points_on_x = []
    points_on_y = []
    for point in points:
        if point[1] == 0:
            points_on_x.append(point)
        if point[0] == 0:
            points_on_y.append(point)
    for point_on_x in points_on_x:
        for point_on_y in points_on_y:
            if (point_on_x[0], point_on_y[1]) in points and (point_on_y[0], point_on_x[1]) in points:
                count += 1
    return count

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
    d = {}
    for i in range(N):
        d[(x[i], y[i])] = 1
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if (x[i], y[j]) in d and (x[j], y[i]) in d:
                ans += 1
    print(ans)
