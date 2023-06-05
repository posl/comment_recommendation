Synthesizing 10/10 solutions

=======
Suggestion 1

def search_pair(x_list):
    pair_list = []
    for i in range(len(x_list)):
        for j in range(len(x_list)):
            if x_list[i] < x_list[j]:
                pair_list.append([x_list[i], x_list[j]])
    return pair_list

=======
Suggestion 2

def solve(n, xs, ys):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if xs[i] == xs[j] or ys[i] == ys[j]:
                count += 1
    return count

=======
Suggestion 3

def calc_rects(n, points):
    rects = 0
    for i in range(n):
        for j in range(i+1, n):
            p1 = points[i]
            p2 = points[j]
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])
            if p3 in points and p4 in points:
                rects += 1
    return rects

=======
Suggestion 4

def get_rects(points):
    points = sorted(points)
    rects = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                rects.append((points[i], points[j]))
    return rects

=======
Suggestion 5

def get_count_of_rectangles(points):
    count = 0
    for point in points:
        x, y = point
        for point2 in points:
            x2, y2 = point2
            if x2 > x and y2 > y:
                if (x, y2) in points and (x2, y) in points:
                    count += 1
    return count/2

=======
Suggestion 6

def get_count(points):
    count = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                for l in range(k+1, len(points)):
                    if is_rectangle(points[i], points[j], points[k], points[l]):
                        count += 1
    return count

=======
Suggestion 7

def find_point():
    n = int(raw_input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = raw_input().split()
        x.append(x1)
        y.append(y1)
    x = map(int,x)
    y = map(int,y)
    x.sort()
    y.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                for k in range(j+1,n):
                    if y[k] == y[j]:
                        for l in range(k+1,n):
                            if y[l] == y[k] and x[l] == x[i]:
                                count += 1
    print count

find_point()

=======
Suggestion 8

def main():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(map(int, raw_input().split()))
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                count += 1
    print count / 2

=======
Suggestion 9

def main():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(map(int, raw_input().split()))
    points = sorted(points, key=lambda x: x[1])
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0]:
                continue
            else:
                for k in range(j+1, n):
                    if points[k][1] == points[j][1]:
                        continue
                    else:
                        for l in range(k+1, n):
                            if points[l][0] == points[i][0]:
                                continue
                            else:
                                if points[i][1] == points[k][1] and points[i][0] == points[l][0] and points[j][0] == points[l][0] and points[j][1] == points[k][1]:
                                    count += 1
    print count

=======
Suggestion 10

def get_input():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, raw_input().split())))
    return points
