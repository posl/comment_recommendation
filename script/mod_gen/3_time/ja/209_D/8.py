def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N)]
    # 隣接リストに道路を追加
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # クエリを受け取る
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # 高橋君の出発点
    start = [q[0] for q in queries]
    # 青木君の出発点
    goal = [q[1] for q in queries]
    # 道路の長さ
    length = [1] * (N-1)
    # 道路の長さを計算
    length = calc_length(graph, length)
    # クエリを処理
    for s, g in zip(start, goal):
        # 道路の長さの差が偶数ならTown、奇数ならRoad
        if (length[s-1] - length[g-1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()