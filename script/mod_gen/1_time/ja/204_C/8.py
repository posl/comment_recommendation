def main():
    N, M = map(int, input().split())
    # 2次元配列を作る
    road = [[0 for i in range(N)] for j in range(N)]
    # 道路の情報を入れる
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1][B-1] = 1
    # 道路の情報を出力する
    #for i in range(N):
    #    print(road[i])
    # スタート地点とゴール地点の組として考えられるものの数をカウントする
    count = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] == 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()