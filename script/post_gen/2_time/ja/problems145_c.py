Synthesizing 10/10 solutions

=======
Suggestion 1

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

import itertools
import numpy as np

ans = 0
for p in itertools.permutations(range(N)):
    for i in range(N-1):
        ans += dist(XY[p[i]],XY[p[i+1]])
ans /= np.math.factorial(N)
print(ans)

from itertools import permutations
from math import sqrt

=======
Suggestion 2

def main():
    import math
    import itertools
    N = int(input())
    city = []
    for i in range(N):
        x, y = map(int, input().split())
        city.append([x, y])
    distance = []
    for i in range(N):
        for j in range(N):
            distance.append(math.sqrt((city[i][0]-city[j][0])**2+(city[i][1]-city[j][1])**2))
    permutation = list(itertools.permutations(distance, N))
    sum = 0
    for i in range(len(permutation)):
        sum += sum(permutation[i])
    print(sum/len(permutation))
main()

=======
Suggestion 3

def main():
    import math
    import itertools
    import sys
    input = sys.stdin.readline

    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = x
        Y[i] = y

    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)

    ans = 0
    for v in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += dist[v[i]][v[i+1]]

    print(ans/math.factorial(N))

=======
Suggestion 4

def main():
    import math
    import itertools
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += math.sqrt((XY[p[i]][0]-XY[p[i+1]][0])**2 + (XY[p[i]][1]-XY[p[i+1]][1])**2)
    print(ans/math.factorial(N))

=======
Suggestion 5

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    import itertools
    dist = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            dist += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
    print(dist/itertools.permutations(range(N)))

=======
Suggestion 6

def main():
    import sys
    import math
    import itertools
    input = sys.stdin.readline
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    # 座標の差の絶対値の平方
    def dist(i, j):
        dx = xy[i][0] - xy[j][0]
        dy = xy[i][1] - xy[j][1]
        return dx**2 + dy**2
    # 経路の長さ
    def route_length(route):
        return sum(dist(i, j) for i, j in zip(route[:-1], route[1:]))
    # 経路の長さの平均値
    def avg_route_length():
        routes = itertools.permutations(range(N))
        return sum(route_length(route) for route in routes) / math.factorial(N)
    print(avg_route_length())

=======
Suggestion 7

def main():
    import sys
    import math
    import itertools

    N = int(sys.stdin.readline())
    xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 町を訪れる経路は全部で N! 通りあります。
    # 1 番目に訪れる町から出発し、2 番目に訪れる町、3 番目に訪れる町、...、を経由し、N 番目に訪れる町に到着するまでの移動距離
    # 町から町への移動は直線移動とします) を、その経路の長さとします。
    # これらの N! 通りの経路の長さの平均値を計算してください。

    # 全ての経路を計算する
    # 1 → 2 → 3 , 1 → 3 → 2 , 2 → 1 → 3 , 2 → 3 → 1 , 3 → 1 → 2 , 3 → 2 → 1 の 6 通り
    # 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 1
    # 1 → 2 → 3 → 4 → 5 → 6 → 8 → 7 → 1
    # 1 → 2 → 3 → 4 → 5 → 8 → 6 → 7 → 1
    # 1 → 2 → 3 → 4 → 5 → 8 → 7 → 6 → 1
    # 1 → 2 → 3 → 4 → 8 → 5 → 6 → 7 → 1
    # 1 → 2 → 3 → 4 → 8 → 5 → 7 → 6 → 1
    # 1 → 2 → 3 → 4 → 8 → 6 → 5 → 7 → 1
    # 1 →

=======
Suggestion 8

def main():
    import math
    import itertools
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    #print(XY)
    L = []
    for i in range(N):
        for j in range(i+1, N):
            L.append(math.sqrt((XY[i][0] - XY[j][0])**2 + (XY[i][1] - XY[j][1])**2))
    #print(L)
    A = list(itertools.permutations(L, len(L)))
    #print(A)
    B = []
    for i in range(len(A)):
        B.append(sum(A[i]))
    #print(B)
    print(sum(B)/len(B))

=======
Suggestion 9

def main():
    N = int(input())
    x_y = [list(map(int, input().split())) for _ in range(N)]

    # 順列を作成
    import itertools
    perm = itertools.permutations(range(N))

    # 距離を計算
    import math
    distance = 0
    for p in perm:
        for i in range(N-1):
            distance += math.sqrt((x_y[p[i]][0]-x_y[p[i+1]][0])**2 + (x_y[p[i]][1]-x_y[p[i+1]][1])**2)

    # 平均値を出力
    print(distance/(math.factorial(N)))

=======
Suggestion 10

def main():
    import sys
    import math
    import itertools

    N = int(sys.stdin.readline())
    xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 順列を列挙
    perm = itertools.permutations(range(1, N))

    # 各順列について、2点間の距離を求める
    ans = 0
    for p in perm:
        d = 0
        for i in range(N-1):
            d += math.sqrt((xy[p[i]][0]-xy[p[i+1]][0])**2 + (xy[p[i]][1]-xy[p[i+1]][1])**2)
        ans += d

    # 平均を求める
    ans = ans / math.factorial(N)
    print(ans)
