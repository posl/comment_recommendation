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

if __name__ == '__main__':
    main()