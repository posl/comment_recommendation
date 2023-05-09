def main():
    N = int(input())
    # レストランのリスト
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append((s, int(p), i+1))
    # レストランのリストをソート
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])
