Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            max_len = max(max_len, ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5)
    print(max_len)

=======
Suggestion 2

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = get_distance(points[i], points[j])
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 3

def max_length(points):
    max_length = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            length = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if length > max_length:
                max_length = length
    return max_length ** 0.5

=======
Suggestion 4

def main():
    num = int(input())
    points = []
    for i in range(num):
        points.append(list(map(int, input().split())))

    max_len = 0
    for i in range(num-1):
        for j in range(i+1, num):
            len = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if len > max_len:
                max_len = len
    print(max_len)

=======
Suggestion 5

def distance(i,j):
    x = abs(i[0]-j[0])
    y = abs(i[1]-j[1])
    return (x**2+y**2)**0.5

=======
Suggestion 6

def getDistance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 7

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(1/2)
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 8

def max_len(points):
    max_len = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            len = points[i].length(points[j])
            if len > max_len:
                max_len = len
    return max_len

=======
Suggestion 9

def main():
    # 读入数据
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    # 求最大距离
    maxd = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            if d > maxd:
                maxd = d
    # 输出结果
    print(maxd)
