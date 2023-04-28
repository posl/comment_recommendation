Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x_list = []
    y_list = []
    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    #print(x_list)
    #print(y_list)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += ((x_list[i]-x_list[j])**2+(y_list[i]-y_list[j])**2)**(1/2)
            #print(sum)
    print(sum/(math.factorial(n)))

=======
Suggestion 2

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())

    def dist(i, j):
        return ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5

    # 階乗
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n - 1)

    # 順列
    def perm(n, r):
        return fact(n) // fact(n - r)

    # 訪れる経路の総数
    def route(n):
        return fact(n)

    # 訪れる経路の総距離
    def route_dist(n):
        if n == 1:
            return 0
        else:
            return route(n - 1) * (route_dist(n - 1) + dist(n - 1, n))

    print(route_dist(n) / route(n))

=======
Suggestion 3

def length(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 4

def main():
    N = int(input())
    town = []
    for i in range(N):
        town.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ((town[j][0]-town[i][0])**2+(town[j][1]-town[i][1])**2)**0.5
    print(ans/N)

=======
Suggestion 5

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

import itertools

n = int(input())
towns = []
for _ in range(n):
    x, y = map(int, input().split())
    towns.append((x,y))

routes = list(itertools.permutations(towns))
sum = 0
for route in routes:
    for i in range(len(route)-1):
        sum += distance(route[i][0], route[i][1], route[i+1][0], route[i+1][1])
print(sum/len(routes))

=======
Suggestion 6

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    # 順列を作る
    def permutation(N, r):
        if r == 0:
            yield []
        else:
            for i in range(N):
                for p in permutation(N, r - 1):
                    if i not in p:
                        yield [i] + p

    # 町を訪れる経路は全部で N! 通りあります。
    # 1 番目に訪れる町から出発し、2 番目に訪れる町、3 番目に訪れる町、...、を経由し、N 番目に訪れる町に到着するまでの移動距離 (町から町への移動は直線移動とします) を、その経路の長さとします。
    # これらの N! 通りの経路の長さの平均値を計算してください。
    total = 0
    count = 0
    for p in permutation(N, N):
        # 経路の長さを計算
        for i in range(1, N):
            total += ((x[p[i - 1]] - x[p[i]]) ** 2 + (y[p[i - 1]] - y[p[i]]) ** 2) ** 0.5
        count += 1
    print(total / count)

=======
Suggestion 7

def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append([x,y])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += ((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)**0.5
    ans /= N
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    data = []
    for i in range(n):
        x, y = map(int, input().split())
        data.append([x, y])

    import itertools
    import math
    sum = 0
    for i in itertools.permutations(data):
        for j in range(n-1):
            sum += math.sqrt((i[j][0]-i[j+1][0])**2 + (i[j][1]-i[j+1][1])**2)
    print(sum/math.factorial(n))

=======
Suggestion 9

def main():
    N = int(input())
    cities = []
    for i in range(N):
        x, y = map(int, input().split())
        cities.append((x, y))

    import itertools
    import math

    # 経路のリストを作成
    routes = list(itertools.permutations(cities))

    # 全経路の距離を計算
    sum = 0
    for route in routes:
        for i in range(len(route) - 1):
            sum += math.sqrt((route[i][0] - route[i + 1][0]) ** 2 + (route[i][1] - route[i + 1][1]) ** 2)

    # 平均を計算
    print(sum / len(routes))

=======
Suggestion 10

def main():
    N = int(input())
    towns = []
    for i in range(N):
        towns.append(list(map(int, input().split())))
    #print(towns)
    import itertools
    all_routes = list(itertools.permutations(range(N), N))
    #print(all_routes)
    sum = 0
    for route in all_routes:
        for i in range(N-1):
            sum += ((towns[route[i]][0] - towns[route[i+1]][0])**2 + (towns[route[i]][1] - towns[route[i+1]][1])**2)**0.5
    print(sum/len(all_routes))
