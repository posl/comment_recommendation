Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** (1 / 2)
    print(ans * 2 / N)

main()

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    # 経路の順列を作成
    import itertools
    routes = list(itertools.permutations(range(n)))

    # 経路の長さのリスト
    route_length_list = []

    # 経路の長さを計算
    for route in routes:
        length = 0
        for i in range(n-1):
            length += ((x[route[i]] - x[route[i+1]])**2 + (y[route[i]] - y[route[i+1]])**2)**(1/2)
        route_length_list.append(length)

    # 平均を求める
    print(sum(route_length_list)/len(route_length_list))

=======
Suggestion 3

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 4

def main():
    N = int(input())
    xy = []
    for _ in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))

    fact = [1]
    for i in range(1, N + 1):
        fact.append(fact[-1] * i)

    sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum += ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5

    print(sum * 2 / fact[N])

=======
Suggestion 5

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    perm = [i for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
    ans *= (N - 1) / (N * math.factorial(N - 1))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    town = []
    for i in range(N):
        x, y = map(int, input().split())
        town.append([x, y])
    path = [i for i in range(N)]
    count = 0
    for i in range(N):
        count += path[i]
    ans = 0
    for i in range(count):
        ans += ((town[path[0]][0] - town[path[1]][0]) ** 2 + (town[path[0]][1] - town[path[1]][1]) ** 2) ** 0.5
        for j in range(N - 2):
            ans += ((town[path[j + 1]][0] - town[path[j + 2]][0]) ** 2 + (town[path[j + 1]][1] - town[path[j + 2]][1]) ** 2) ** 0.5
        path = path[1:] + path[:1]
    ans = ans / (N * (N - 1) / 2)
    print(ans)

main()

=======
Suggestion 7

def main():
    import sys
    from itertools import permutations
    from math import sqrt
    input = sys.stdin.readline
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for p in permutations(range(N)):
        for i in range(N - 1):
            ans += sqrt((X[p[i]] - X[p[i + 1]]) ** 2 + (Y[p[i]] - Y[p[i + 1]]) ** 2)
    print(ans / N)

=======
Suggestion 8

def main():
    import sys
    from itertools import permutations
    import math

    N = int(input())
    towns = []
    for i in range(N):
        x, y = map(int, input().split())
        towns.append((x, y))

    paths = permutations(towns)
    total = 0
    for path in paths:
        for i in range(N - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            total += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(total / math.factorial(N))

=======
Suggestion 9

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

=======
Suggestion 10

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]

    # パスの長さ
    def path_len(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length

    # パスの総和
    def path_sum(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length

    # パスの平均
    def path_avg(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length / len(path)

    # パスの総和
    def path_sum(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length

    # パスの平均
    def path_avg(path):
        length = 0
        for i in range(len(path) - 1):
            x1, y1 = xy[path[i]]
            x2, y2 = xy[path[i + 1]]
            length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length
