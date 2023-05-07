def main():
    N, M = map(int, input().split())
    # 都市と道路の接続をリストに格納
    road = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A - 1].append(B - 1)
        road[B - 1].append(A - 1)
    # 接続数と都市番号を出力
    for i in range(N):
        print(len(road[i]), end = " ")
        for j in road[i]:
            print(j + 1, end = " ")
        print()
