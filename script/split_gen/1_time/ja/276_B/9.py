def main():
    N, M = map(int, input().split())
    # 1. 都市と都市をつなぐ道路をリスト化
    roads = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        roads[A-1][B-1] = 1
        roads[B-1][A-1] = 1
    # 2. 都市と都市をつなぐ道路を集計
    for i in range(N):
        # 都市と都市をつなぐ道路の数だけ、都市をリスト化
        roads_list = []
        for j in range(N):
            if roads[i][j] == 1:
                roads_list.append(j+1)
        # 都市をリスト化
        roads_list.insert(0, len(roads_list))
        # 都市をリスト化したものを出力
        print(*roads_list)
