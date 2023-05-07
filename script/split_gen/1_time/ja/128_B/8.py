def main():
    N = int(input())
    # レストランの名前と点数を格納するリスト
    restaurant = []
    for i in range(N):
        # レストランの名前と点数を格納
        restaurant.append(input().split())
        # レストランの名前を格納
        restaurant[i][0] = restaurant[i][0] + ' ' + str(i + 1)
        # レストランの点数を格納
        restaurant[i][1] = int(restaurant[i][1])
    # レストランの名前を辞書順にソート
    restaurant.sort(key=lambda x: x[0])
    # レストランの点数を降順にソート
    restaurant.sort(key=lambda x: x[1], reverse=True)
    # レストランの名前を表示
    for i in range(N):
        print(restaurant[i][0].split()[1])
