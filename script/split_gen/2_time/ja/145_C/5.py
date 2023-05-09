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
