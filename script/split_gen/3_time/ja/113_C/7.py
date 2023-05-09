def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(M)]
    # 都道府県ごとに誕生年でソート
    city.sort(key=lambda x: x[1])
    # 都道府県ごとの誕生年のリスト
    birth = [[] for _ in range(N + 1)]
    for i in range(M):
        birth[city[i][0]].append(city[i][1])
    # 都道府県ごとに誕生年の順位を求める
    rank = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        birth[i].sort()
        for j in range(len(birth[i])):
            rank[i].append(birth[i].index(city[i - 1][1]) + 1)
    # 認識番号を求める
    for i in range(M):
        print(str(city[i][0]).zfill(6) + str(rank[city[i][0]][i]).zfill(6))
