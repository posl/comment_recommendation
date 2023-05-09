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
