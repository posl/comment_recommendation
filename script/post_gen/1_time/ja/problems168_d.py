Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = [0] * N
    ans[0] = -1
    for i in range(M):
        if A[i] == 1:
            ans[B[i] - 1] = 1
        if B[i] == 1:
            ans[A[i] - 1] = 1

    if 0 in ans:
        print('No')
    else:
        print('Yes')
        for i in range(N - 1):
            print(ans[i])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 部屋に通路が何本あるかを数える
    count = [0] * (N + 1)
    for i in range(M):
        count[A[i]] += 1
        count[B[i]] += 1
    # 部屋に通路が何本あるかを数える
    count = [0] * (N + 1)
    for i in range(M):
        count[A[i]] += 1
        count[B[i]] += 1
    # 部屋に通路が1本しかない場合は、その部屋とその通路の組み合わせを出力する
    # 部屋に通路が2本以上ある場合は、部屋1とその通路の組み合わせを出力する
    print('Yes')
    for i in range(1, N + 1):
        if count[i] == 1:
            for j in range(M):
                if A[j] == i or B[j] == i:
                    print(j + 1)
                    break
        else:
            for j in range(M):
                if A[j] == i and B[j] == 1:
                    print(j + 1)
                    break
                if B[j] == i and A[j] == 1:
                    print(j + 1)
                    break

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * N
    for i in range(M):
        if A[i] == 1:
            ans[B[i]-1] = A[i]
        elif B[i] == 1:
            ans[A[i]-1] = B[i]
    for i in range(M):
        if ans[A[i]-1] == 0:
            ans[A[i]-1] = B[i]
        elif ans[B[i]-1] == 0:
            ans[B[i]-1] = A[i]
    for i in range(N):
        if ans[i] == 0:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(ans[i])

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [1 for i in range(N)]
    for i in range(M):
        if ans[A[i]-1] != A[i]:
            ans[B[i]-1] = A[i]
        else:
            ans[B[i]-1] = B[i]
    print("Yes")
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    ans = [0] * (N + 1)
    ans[1] = 1
    q = [1]
    while q:
        v = q.pop()
        for nv in G[v]:
            if ans[nv] == 0:
                ans[nv] = v
                q.append(nv)
    if 0 in ans[2:]:
        print('No')
    else:
        print('Yes')
        for i in range(2, N + 1):
            print(ans[i])

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    # 1からの距離
    dist = [-1]*(N+1)
    dist[1] = 0
    # BFS
    q = deque([1])
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = v
            q.append(nv)
    # 出力
    if -1 in dist[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, N+1):
            print(dist[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 部屋1から各部屋への最短距離
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    # BFS
    q = [1]
    while q:
        v = q.pop(0)
        for nv in graph[v]:
            if dist[nv] == float('inf'):
                dist[nv] = dist[v] + 1
                q.append(nv)
    # 部屋1以外の部屋に道しるべを置く
    ans = [0] * (N+1)
    for i in range(2, N+1):
        for nv in graph[i]:
            if dist[nv] == dist[i] - 1:
                ans[i] = nv
                break
    # 出力
    print('Yes')
    for i in range(2, N+1):
        print(ans[i])

main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    road = []
    for i in range(M):
        a, b = map(int, input().split())
        road.append([a, b])
    #print(road)
    road.sort(key=lambda x: x[0])
    #print(road)
    ans = []
    for i in range(N):
        ans.append(1)
    for i in range(M):
        if road[i][0] == 1:
            ans[road[i][1] - 1] = 1
    for i in range(M):
        if road[i][0] != 1:
            ans[road[i][1] - 1] = road[i][0]
    print("Yes")
    for i in range(N):
        print(ans[i])

=======
Suggestion 9

def main():
    from sys import stdin
    readline = stdin.readline

    N, M = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(M)]

    # 1から各部屋にたどり着くまでの経路を求める
    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)
        route[b].append(a)

    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)
        route[b].append(a)

    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)
        route[b].append(a)

    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)
        route[b].append(a)

    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)
        route[b].append(a)

    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)
        route[b].append(a)

    # 1から各部屋にたどり着くまでの経路を求める
    route = [[] for _ in range(N+1)]
    for a, b in AB:
        route[a].append(b)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M, AB)
    #print(AB)
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])

    #print(AB[0])
    #print(AB[1])
    #print(AB[2])
    #print(AB[3])
    #print(AB[4])
    #print(AB[5])
    #print(AB[6])
    #print(AB[7])
    #print(AB[8])
    #print(AB[9])

    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])

    #print(AB[0][0])
    #print
