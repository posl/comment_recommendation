Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    ans = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        ans[a-1].append(b)
        ans[b-1].append(a)
    for a in ans:
        print(len(a), *sorted(a))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        road[A - 1].append(B)
        road[B - 1].append(A)
    for r in road:
        print(len(r), *sorted(r))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        a[A - 1].append(B)
        a[B - 1].append(A)
    for i in range(N):
        a[i].sort()
        print(len(a[i]), *a[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)

    for i in range(N):
        road[i].sort()
        print(len(road[i]), end=" ")
        for j in road[i]:
            print(j+1, end=" ")
        print()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)
    for i in range(N):
        print(len(edges[i]), end=' ')
        for j in sorted(edges[i]):
            print(j + 1, end=' ')
        print()

=======
Suggestion 6

def main():
    from collections import deque
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    for i in range(N):
        road[i].sort()
        road[i] = deque(road[i])
    for i in range(N):
        d = len(road[i])
        print(d, end=" ")
        for _ in range(d):
            print(road[i].popleft()+1, end=" ")
        print()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # 都市と道路の関係をリストで保持
    roads = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        roads[a - 1].append(b - 1)
        roads[b - 1].append(a - 1)
    # 都市と道路の関係を出力
    for i in range(N):
        print(len(roads[i]) + 1, end = ' ')
        for j in range(len(roads[i])):
            print(roads[i][j] + 1, end = ' ')
        print()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 都市と道路の隣接リストを作る
    city = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        city[a-1].append(b-1)
        city[b-1].append(a-1)
    # 都市iと直接結ばれている都市の数と、都市iと直接結ばれている都市を出力
    for i in range(N):
        print(len(city[i]), end='')
        for j in city[i]:
            print(' ' + str(j+1), end='')
        print()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 都市をキーにして、道路で直接結ばれた都市のリストを値とする辞書を作成
    d = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().split())
        d[A].append(B)
        d[B].append(A)
    # 道路で直接結ばれた都市のリストの要素数と、その都市の番号を出力
    for i in range(1, N + 1):
        print(len(d[i]), *sorted(d[i]))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 都市と道路の関係を表すリスト
    # 都市iと道路で直接結ばれた都市の数
    d = [0] * N
    # 都市iと道路で直接結ばれた都市のリスト
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        d[A-1] += 1
        d[B-1] += 1
        a[A-1].append(B)
        a[B-1].append(A)
    for i in range(N):
        a[i] = sorted(a[i])
        print(d[i], *a[i])
