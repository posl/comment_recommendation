def main():
    N, M = map(int, input().split())
    # 都市と道路の関係をリストで持つ
    # 都市の番号をリストのインデックスとして、
    # 都市に直結する道路の都市番号をリストに格納する
    # 都市1から都市2への道路があれば、
    # 都市1のリストに都市2を追加し、
    # 都市2のリストに都市1を追加する
    road = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    # 都市の直結数を出力する
    for i in range(N):
        print(len(road[i]), end="")
        for j in range(len(road[i])):
            print(" {}".format(road[i][j]+1), end="")
        print()
