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
