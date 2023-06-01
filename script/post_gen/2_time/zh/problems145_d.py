Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 2

def main():
    # 读入数据
    with open('problems145_c.txt', 'r') as f:
        n = int(f.readline())
        xy_list = []
        for i in range(n):
            xy_list.append(f.readline().split())

    # 计算距离
    distance_list = []
    for i in range(n):
        for j in range(i+1, n):
            distance = ((int(xy_list[i][0]) - int(xy_list[j][0])) ** 2 + (int(xy_list[i][1]) - int(xy_list[j][1])) ** 2) ** 0.5
            distance_list.append(distance)

    # 计算平均距离
    print(sum(distance_list) / len(distance_list))

=======
Suggestion 3

def main():
    import sys
    N = int(sys.stdin.readline())
    towns = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        towns.append(list(map(int, line.split())))

    import itertools
    import math
    total = 0
    for i in itertools.permutations(range(N)):
        for j in range(N-1):
            total += math.sqrt((towns[i[j]][0]-towns[i[j+1]][0])**2 + (towns[i[j]][1]-towns[i[j+1]][1])**2)
    print(total/math.factorial(N))

=======
Suggestion 4

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 5

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

=======
Suggestion 6

def main():
    return

=======
Suggestion 7

def get_distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

=======
Suggestion 8

def getDistance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
