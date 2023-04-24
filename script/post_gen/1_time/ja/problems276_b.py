Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    for i in range(1, N+1):
        d = 0
        for j in range(M):
            if i == A[j]:
                d += 1
            elif i == B[j]:
                d += 1
        print(d, end=" ")
        for j in range(M):
            if i == A[j]:
                print(B[j], end=" ")
            elif i == B[j]:
                print(A[j], end=" ")
        print()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        road[A-1].append(B)
        road[B-1].append(A)
    for i in range(N):
        road[i].sort()
        print(len(road[i]), end = ' ')
        print(*road[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    city = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        city[A-1].append(B)
        city[B-1].append(A)
    for i in range(N):
        city[i].sort()
        print(len(city[i]), *city[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 都市と道路の関係をリストで作成
    city = [[] for i in range(N)]
    for i in range(M):
        city[A[i] - 1].append(B[i])
        city[B[i] - 1].append(A[i])

    # 都市と道路の関係を出力
    for i in range(N):
        print(len(city[i]), end = ' ')
        for j in range(len(city[i])):
            print(city[i][j], end = ' ')
        print()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    # 都市iと道路で直接結ばれた都市の数
    d = [0] * N
    # 都市iと道路で直接結ばれた都市の集合
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        d[A-1] += 1
        d[B-1] += 1
        a[A-1].append(B)
        a[B-1].append(A)
    for i in range(N):
        print(d[i], *sorted(a[i]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    # 都市iと道路で直接結ばれた都市を格納するリスト
    city = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        city[A - 1].append(B - 1)
        city[B - 1].append(A - 1)
    for i in range(N):
        city[i].sort()
        print(len(city[i]), end=" ")
        for j in city[i]:
            print(j + 1, end=" ")
        print()

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 都市ごとに道路で直接結ばれている都市の数をカウントする
    # 都市iと道路で直接結ばれている都市の数をd_iとすると、
    # 都市iと道路で直接結ばれている都市の番号をa_{i, 1}, ..., a_{i, d_i}とする
    # つまり、都市iと道路で直接結ばれている都市の番号は、a_{i, 1}, ..., a_{i, d_i}のd_i+1個の整数となる
    # このとき、a_{i, 1}, ..., a_{i, d_i}は昇順に並んでいなければならない
    # つまり、a_{i, 1} <= a_{i, 2} <= ... <= a_{i, d_i}となる
    # また、都市iと道路で直接結ばれている都市の数は、d_i >= 0となる
    # つまり、d_i+1個の整数は、d_i >= 0, a_{i, 1} <= a_{i, 2} <= ... <= a_{i, d_i}を満たす
    # 以上より、都市iと道路で直接結ばれている都市の数をd_iとすると、
    # 都市iと道路で直接結ばれている都市の番号をa_{i, 1}, ..., a_{i, d_i}とすると、
    # 都市iと道路で直接結ばれている都市の番号は、d_i+1個の整数となり、
    # このとき、a_{i, 1}, ..., a_{i, d_i}は昇順に並んでいな

=======
Suggestion 9

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

=======
Suggestion 10

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
