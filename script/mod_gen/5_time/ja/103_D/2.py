def solve():
    # 入力
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # 各島について、西から何番目の島かを求める
    # 各島について、西から何番目の島かを求める
    west_island = [0] * (N + 1)
    for i, (a, b) in enumerate(AB):
        west_island[a] = i + 1
        west_island[b] = i + 1
    # 西から何番目の島かを求める
    west_island = [0] * (N + 1)
    for i, (a, b) in enumerate(AB):
        west_island[a] = i + 1
        west_island[b] = i + 1
    # 区間を求める
    # 区間を求める
    intervals = []
    start = -1
    for i, island in enumerate(west_island):
        if island == 0:
            continue
        if start == -1:
            start = i
            continue
        if west_island[i - 1] != island:
            intervals.append((start, i - 1))
            start = i
    if start != -1:
        intervals.append((start, N))
    # 区間の個数を求める
    # 区間の個数を求める
    ans = 0
    for i in intervals:
        ans += 1
    print(ans - 1)

if __name__ == '__main__':
    solve()