Synthesizing 10/10 solutions

=======
Suggestion 1

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 2

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 3
    a = [[0,0],[1,0],[0,1]]
    print(a)

    #print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    #print(towns)

    def calc_distance(a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

    def calc_path_distance(towns, path):
        distance = 0
        for i in range(N-1):
            distance += calc_distance(towns[path[i]], towns[path[i+1]])
        return distance

    def calc_average_distance(towns):
        path = list(range(N))
        total_distance = 0
        for i in range(N):
            for j in range(N):
                path[i], path[j] = path[j], path[i]
                total_distance += calc_path_distance(towns, path)
                path[i], path[j] = path[j], path[i]
        return total_distance / (N * (N-1))

    print(calc_average_distance(towns))

=======
Suggestion 4

def main():
    N = int(input())
    cities = []
    for i in range(N):
        cities.append(list(map(int, input().split())))
    #print(cities)
    import itertools
    import math
    sum = 0
    count = 0
    for i in itertools.permutations(cities, N):
        #print(i)
        for j in range(N-1):
            sum += math.sqrt((i[j][0]-i[j+1][0])**2+(i[j][1]-i[j+1][1])**2)
        count += 1
    print(sum/count)
main()

=======
Suggestion 5

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

import itertools

l = list(itertools.permutations(range(n)))
ans = 0
for i in range(len(l)):
    for j in range(n-1):
        ans += dist(x[l[i][j]],y[l[i][j]],x[l[i][j+1]],y[l[i][j+1]])
print(ans/len(l))

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    import itertools
    import math
    l = list(itertools.permutations(range(n)))
    total = 0
    for i in range(len(l)):
        for j in range(n-1):
            total += math.sqrt((x[l[i][j]]-x[l[i][j+1]])**2 + (y[l[i][j]]-y[l[i][j+1]])**2)
    print(total/len(l))
main()

=======
Suggestion 7

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 8

def getDistances(start, points, distance):
    if len(points) == 0:
        return distance
    else:
        distances = []
        for i in range(len(points)):
            distances.append(getDistances(points[i], points[:i] + points[i+1:], distance + ((start[0] - points[i][0]) ** 2 + (start[1] - points[i][1]) ** 2) ** 0.5))
        return distances

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

distances = []
for i in range(N):
    distances.append(getDistances(points[i], points[:i] + points[i+1:], 0))

sum = 0
for i in range(N):
    for j in range(len(distances[i])):
        sum += distances[i][j]

print(sum / (N * (N - 1)))

=======
Suggestion 9

def main():
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += ((towns[i][0] - towns[j][0])**2 + (towns[i][1] - towns[j][1])**2)**0.5
    print(sum * 2 * math.factorial(N-1) / math.factorial(N))

=======
Suggestion 10

def main():
    N = int(input())
    xy = []
    for i in range(N):
        x,y = map(int,input().split())
        xy.append([x,y])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**(1/2)
    ans /= N
    print(ans)
