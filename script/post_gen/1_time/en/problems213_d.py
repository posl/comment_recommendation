Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    roads = {}
    for i in range(n-1):
        a, b = map(int, input().split())
        if a in roads:
            roads[a].append(b)
        else:
            roads[a] = [b]
        if b in roads:
            roads[b].append(a)
        else:
            roads[b] = [a]
    #print(roads)
    visited = [1]
    stack = [1]
    while stack:
        node = stack.pop()
        if node in roads:
            for next in roads[node]:
                if next not in visited:
                    stack.append(next)
                    visited.append(next)
    print(*visited)

=======
Suggestion 2

def main():
    N = int(input())
    A = list()
    B = list()
    for i in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(len(A))
    #print(len(B))
    visited = [0] * N
    visited[0] = 1
    #print(visited)
    route = [1]
    #print(route)
    for i in range(N-1):
        if B[i] == route[-1]:
            route.append(A[i])
        elif A[i] == route[-1]:
            route.append(B[i])
        else:
            continue
    #print(route)
    route.append(1)
    print(*route)

=======
Suggestion 3

def main():
    n = int(input())
    roads = {}
    for i in range(n-1):
        a,b = map(int, input().split())
        if a in roads:
            roads[a].append(b)
        else:
            roads[a] = [b]
        if b in roads:
            roads[b].append(a)
        else:
            roads[b] = [a]
    for i in roads:
        roads[i].sort()
    stack = [1]
    visited = [1]
    while stack:
        current = stack.pop()
        print(current, end=" ")
        for i in roads[current]:
            if i not in visited:
                stack.append(i)
                visited.append(i)
    print()

=======
Suggestion 4

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    G = [[] for _ in range(N+1)]
    for a,b in AB:
        G[a].append(b)
        G[b].append(a)

    from collections import deque
    q = deque([1])
    visited = [False] * (N+1)
    visited[1] = True
    ans = []
    while q:
        x = q.popleft()
        ans.append(x)
        for y in G[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
                break
        else:
            if x == 1:
                break
            q.appendleft(x)

    print(*ans)

=======
Suggestion 5

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    print(' '.join(str(x) for x in [1] + [AB[i][1] for i in range(N-1)] + [1]))

=======
Suggestion 6

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    road = [[] for _ in range(n+1)]
    for a, b in ab:
        road[a].append(b)
        road[b].append(a)
    for i in range(n+1):
        road[i].sort()
    ans = []
    stack = [1]
    while stack:
        now = stack.pop()
        ans.append(now)
        for next in road[now]:
            if next not in ans:
                stack.append(next)
    print(*ans)

=======
Suggestion 7

def resolve():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append((b-1, i))
        G[b-1].append((a-1, i))

    ans = []
    q = deque([0])
    seen = [False] * N
    while q:
        u = q.popleft()
        ans.append(u+1)
        seen[u] = True
        for v, i in G[u]:
            if seen[v]:
                continue
            q.append(v)
            ans.append(u+1)
    print(*ans)

=======
Suggestion 8

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h = [int(input()) for i in range(n)]
    n = 4
    h = [1, 2, 2, 1]
    #h = [int(input()) for i in range(n)]
    #a = list(map(int, input().split()))
    #s = input()
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h = [int(input()) for i in range(n)]
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h = [int(input()) for i in range(n)]
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h = [int(input()) for i in range(n)]
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h = [int(input()) for i in range(n)]
    #n = int(input())
    #a = list(map(int, input().split()))
    #s = input()
    #h = [int(input()) for i in range(n)]
    #n =

=======
Suggestion 9

def main():
    N = int(input())
    AB = []
    for i in range(N-1):
        AB.append([int(i) for i in input().split()])
    AB.sort()
    #print(AB)
    A = [AB[0][0]]
    B = [AB[0][1]]
    for i in range(1,N-1):
        if AB[i][0] in B:
            A.append(AB[i][0])
            B.append(AB[i][1])
        else:
            A.append(AB[i][1])
            B.append(AB[i][0])
    A.append(AB[N-2][1])
    #print(A)
    print(*A, sep=' ')

main()

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    # 1. 隣接リストを作る
    # 2. 深さ優先探索で順番に訪れる都市を求める
    # 3. 1 が出てきたら終了

    # 隣接リストを作る
    adjList = [[] for _ in range(N+1)]
    for a, b in AB:
        adjList[a].append(b)
        adjList[b].append(a)

    # 深さ優先探索で順番に訪れる都市を求める
    visited = [False] * (N+1)
    visited[1] = True
    dfs(adjList, 1, visited, [1])
