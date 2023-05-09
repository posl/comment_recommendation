def solve():
    # 入力
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append([i + 1, S, int(P)])
    # 処理
    restaurants = sorted(restaurants, key=lambda x: (x[1], -x[2]))
    # 出力
    for restaurant in restaurants:
        print(restaurant[0])

if __name__ == '__main__':
    solve()