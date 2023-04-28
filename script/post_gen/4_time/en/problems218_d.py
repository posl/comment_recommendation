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

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x and y[j] in y:
                    ans += 1
            elif x[i] > x[j] and y[i] > y[j]:
                if x[j] in x and y[i] in y:
                    ans += 1

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if (x[i] == x[j] and y[i] == y[k] and x[l] == x[k] and y[l] == y[j]) or (x[i] == x[k] and y[i] == y[j] and x[l] == x[j] and y[l] == y[k]):
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points = set(points)
    ans = 0
    for x1, y1 in points:
        for x2, y2 in points:
            if x1 < x2 and y1 < y2:
                if (x1, y2) in points and (x2, y1) in points:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x,y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                    ans += 1
    print(ans)

=======
Suggestion 5

def get_number_of_rectangles(points):
    """
    >>> get_number_of_rectangles([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)])
    3
    >>> get_number_of_rectangles([(0, 1), (1, 2), (2, 3), (3, 4)])
    0
    >>> get_number_of_rectangles([(0, 1), (1, 0), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)])
    1
    """
    # Write your code here
    result = 0
    return result

=======
Suggestion 6

def get_input():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    return n, xy

=======
Suggestion 7

def solve():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points = set(points)
    answer = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if (x1, y2) in points and (x2, y1) in points:
                answer += 1
    print(answer)

=======
Suggestion 8

def main():
    N = int(input())
    points = []
    for i in range(N):
        point = list(map(int, input().split()))
        points.append(point)
    points.sort()
    #print(points)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                    count += 1
    print(count)

=======
Suggestion 9

def get_input():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    return N, points

=======
Suggestion 10

def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    points_set = set(points)
    points_dict = {}
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                p1 = points[i]
                p2 = points[j]
                if p1[0] == p2[0]:
                    p1, p2 = p2, p1
                if p1[0] < p2[0]:
                    if p1[1] < p2[1]:
                        p3 = (p2[0], p1[1])
                        p4 = (p1[0], p2[1])
                    else:
                        p3 = (p2[0], p2[1])
                        p4 = (p1[0], p1[1])
                else:
                    if p1[1] < p2[1]:
                        p3 = (p1[0], p1[1])
                        p4 = (p2[0], p2[1])
                    else:
                        p3 = (p1[0], p2[1])
                        p4 = (p2[0], p1[1])
                if p3 in points_set and p4 in points_set:
                    if p1 not in points_dict:
                        points_dict[p1] = set()
                    points_dict[p1].add((p3, p4))
    count = 0
    for p1 in points_dict:
        for p2 in points_dict[p1]:
            count += len(points_dict[p1] & points_dict[p2])
    print(count//2)
