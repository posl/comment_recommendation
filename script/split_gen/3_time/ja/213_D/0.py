def main():
    N = int(input())
    A = [0] * (N - 1)
    B = [0] * (N - 1)
    for i in range(N - 1):
        A[i], B[i] = map(int, input().split())
    # 都市と都市のつながりを辞書型で作成
    city = {}
    for i in range(N - 1):
        if A[i] in city:
            city[A[i]].append(B[i])
        else:
            city[A[i]] = [B[i]]
        if B[i] in city:
            city[B[i]].append(A[i])
        else:
            city[B[i]] = [A[i]]
    # 都市を訪れたかどうかのリスト
    visit = [False] * (N + 1)
    # 出発地点を1とする
    start = 1
    # 現在地を1とする
    now = 1
    # 経路を保存するリスト
    route = [now]
    # 現在地を訪れたことを記録
    visit[now] = True
    while True:
        # 現在地から行ける都市を取得
        next_city = city[now]
        # 行ける都市のうち未訪問の都市を取得
        next_city = [i for i in next_city if visit[i] == False]
        # 行ける都市がない場合
        if len(next_city) == 0:
            # 現在地が出発地点なら終了
            if now == start:
                break
            # 現在地が出発地点でなければ、現在地を訪れた直前の都市に戻る
            else:
                now = route[-2]
                route.append(now)
        # 行ける都市がある場合
        else:
            # 行ける都市のうち番号が一番小さい都市に移動
            next_city = min(next_city)
            now = next_city
            route.append(now
