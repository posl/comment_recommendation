def main():
    N, M = map(int, input().split())
    # 都市間の道路の数を格納するリスト
    road = [0] * N
    # 都市間の道路の数をカウント
    for i in range(M):
        a, b = map(int, input().split())
        road[a - 1] += 1
        road[b - 1] += 1
    # 都市間の道路の数を出力
    for i in range(N):
        print(road[i], end = " ")
        for j in range(N):
            if road[j] == i + 1:
                print(j + 1, end = " ")
        print()

if __name__ == '__main__':
    main()