def calc_area(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
