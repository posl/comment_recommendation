Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # 都市の隣接リストを作成
    city = [[] for _ in range(N)]
    for i in range(M):
        city[A[i] - 1].append(B[i])
        city[B[i] - 1].append(A[i])

    # 隣接リストを昇順にソート
    for i in range(N):
        city[i].sort()

    # 出力
    for i in range(N):
        print(len(city[i]), end=' ')
        for j in range(len(city[i])):
            print(city[i][j], end=' ')
        print()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M, A, B)

    # 都市をキーに、道路で直接結ばれた都市を値に持つ辞書を作成する
    cities = {}
    for i in range(M):
        if A[i] not in cities:
            cities[A[i]] = [B[i]]
        else:
            cities[A[i]].append(B[i])
        if B[i] not in cities:
            cities[B[i]] = [A[i]]
        else:
            cities[B[i]].append(A[i])
    #print(cities)

    # 都市の数だけループ
    for i in range(1, N+1):
        # 都市 i と道路で直接結ばれた都市が d_i 個あるとし、それらを昇順に都市 a_{i, 1}, ..., a_{i, d_i} とおく。
        # 都市 i と道路で直接結ばれた都市がない場合
        if i not in cities:
            print(0)
        else:
            # 都市 i と道路で直接結ばれた都市がある場合
            # それらを昇順に都市 a_{i, 1}, ..., a_{i, d_i} とおく。
            print(len(cities[i]), ' '.join(map(str, sorted(cities[i]))))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    path = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        path[a-1].append(b)
        path[b-1].append(a)

    for i in range(n):
        print(len(path[i]), *sorted(path[i]))

=======
Suggestion 4

def main():
    n, m = list(map(int, input().strip().split()))
    road = [[] for i in range(n)]
    for i in range(m):
        a, b = list(map(int, input().strip().split()))
        road[a-1].append(b)
        road[b-1].append(a)
    for i in range(n):
        print(len(road[i]), end=" ")
        print(*sorted(road[i]))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    road = []
    for i in range(m):
        a, b = map(int, input().split())
        road.append([a, b])

    for i in range(1, n+1):
        ans = []
        for j in range(m):
            if i in road[j]:
                ans.append(road[j][0]) if road[j][1] == i else ans.append(road[j][1])
        ans.sort()
        ans.insert(0, len(ans))
        print(*ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())

    # 都市 i と道路で直接結ばれた都市が d_i 個あるとし、それらを昇順に都市 a_{i, 1}, ..., a_{i, d_i} とおく。
    # i (1 ≦ i ≦ N) 行目には、d_i + 1 個の整数 d_i, a_{i, 1}, ..., a_{i, d_i} を、この順番で空白区切りで出力せよ。

    # 都市iと道路で直接結ばれた都市がd_i個あるとし、それらを昇順に都市a_{i,1}, ..., a_{i,d_i}とおく。
    # i(1 ≦ i ≦ N)行目には、d_i + 1個の整数d_i, a_{i,1}, ..., a_{i,d_i}を、この順番で空白区切りで出力せよ。

    # 都市iと道路で直接結ばれた都市がd_i個あるとし、それらを昇順に都市a_{i,1}, ..., a_{i,d_i}とおく。
    # i(1 ≦ i ≦ N)行目には、d_i + 1個の整数d_i, a_{i,1}, ..., a_{i,d_i}を、この順番で空白区切りで出力せよ。

    # 都市iと道路で直接結ばれた都市がd_i個あるとし、それらを昇順に都市a_{i,1}, ..., a_{i,d_i}とおく。
    # i(1 ≦ i ≦ N)行目には、d_i + 1個の整数d_i, a_{i,1}, ..., a_{i,d_i}を、この順番で空白区切りで出力せよ。

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort()
    ans = [[] for _ in range(n)]
    for a, b in ab:
        ans[a-1].append(b)
        ans[b-1].append(a)
    for i in range(n):
        print(len(ans[i]), *ans[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))

    cities = [[] for i in range(N)]
    for road in roads:
        cities[road[0] - 1].append(road[1])
        cities[road[1] - 1].append(road[0])

    for city in cities:
        print(len(city), *city)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    #print(N, M)
    #print(AB)

    A = [0] * N
    B = [0] * N
    for i in range(M):
        A[AB[i][0] - 1] += 1
        B[AB[i][1] - 1] += 1

    #print(A)
    #print(B)

    for i in range(N):
        print(A[i] + B[i])

main()

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    road = [list(map(int, input().split())) for i in range(m)]
    road.sort()
    #print(road)
    city = [0]*n
    #print(city)
    for i in range(m):
        city[road[i][0]-1] += 1
        city[road[i][1]-1] += 1
    #print(city)
    for i in range(n):
        print(city[i])
