Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(1, N+1):
        ans = [0] * (N+1)
        for j in range(M):
            if A[j] == i:
                ans[B[j]] += 1
            elif B[j] == i:
                ans[A[j]] += 1
        print(sum(ans), end="")
        for j in range(1, N+1):
            if ans[j] == 1:
                print(" " + str(j), end="")
        print()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    for i in range(N):
        road[i].sort()
        print(len(road[i]), *road[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    for i in range(1, N + 1):
        print(len(G[i]), *sorted(G[i]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    road = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        road[a].append(b)
        road[b].append(a)
    for i in range(1, N+1):
        road[i].sort()
        print(len(road[i]), *road[i])

=======
Suggestion 5

def main():
    N,M=map(int,input().split())
    road=[[] for _ in range(N)]
    for _ in range(M):
        a,b=map(int,input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    for i in range(N):
        road[i].sort()
        print(len(road[i]),end=" ")
        for j in road[i]:
            print(j+1,end=" ")
        print()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    roads = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        roads[a] += 1
        roads[b] += 1
    for i in range(1, N + 1):
        print(roads[i], end = " ")
        for j in range(1, N + 1):
            if i != j and roads[j] >= 1:
                print(j, end = " ")
        print()

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    d = [0] * N
    a = [[] for _ in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        d[x - 1] += 1
        d[y - 1] += 1
        a[x - 1].append(y - 1)
        a[y - 1].append(x - 1)
    for i in range(N):
        a[i].sort()
    for i in range(N):
        print(d[i], *map(lambda x: x + 1, a[i]))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 都市間の道路の数を格納するリスト
    road = [0] * N
    # 都市間の道路の数をカウント
    for i in range(M):
        a, b = map(int, input().split())
        road[a - 1] += 1
        road[b - 1] += 1
    # 都市間の道路の数を出力
    for i in range(N):
        print(road[i], end = " ")
        for j in range(N):
            if road[j] == i + 1:
                print(j + 1, end = " ")
        print()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 都市をkeyとして、都市と直接つながっている都市の数と、直接つながっている都市をvalueとして辞書を作成
    dic = {}
    for i in range(1, N+1):
        dic[i] = [0, []]
    for i in range(M):
        A, B = map(int, input().split())
        dic[A][0] += 1
        dic[B][0] += 1
        dic[A][1].append(B)
        dic[B][1].append(A)
    # 都市と直接つながっている都市をソート
    for i in range(1, N+1):
        dic[i][1].sort()
    # 出力
    for i in range(1, N+1):
        print(dic[i][0], end="")
        for j in dic[i][1]:
            print(" " + str(j), end="")
        print()

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    # 都市を頂点とす�
