Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    N, M = map(int, input().split())
    #print(N,M)

=======
Suggestion 2

def main():
    #读取数据
    N, M = map(int, input().split())
    #print(N, M)
    #print(type(N), type(M))
    #print(N, M)
    #A, B = map(int, input().split())
    #print(A, B)
    #print(type(A), type(B))
    #print(A, B)

=======
Suggestion 3

def main():
    N,M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(list(map(int, input().split())))
    print(len(a))
    return

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j:
                if a.count(i) + b.count(i) == a.count(j) + b.count(j) == 0:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
    else:
        A = list()
        B = list()
        for i in range(M):
            a, b = map(int, input().split())
            A.append(a)
            B.append(b)
        # print(A)
        # print(B)
        for i in range(M):
            A.append(B[i])
            B.append(A[i])
        # print(A)
        # print(B)
        C = [0 for i in range(N)]
        for i in range(M * 2):
            C[A[i] - 1] += 1
        # print(C)
        sum = 0
        for i in range(N):
            sum += C[i] * (C[i] - 1) / 2
        print(int(sum))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(roads)

    # 从任意城市出发，能到达的城市
    can_reach = [set() for _ in range(N)]
    for road in roads:
        can_reach[road[0]-1].add(road[1]-1)
    # print(can_reach)

    # 从任意城市出发，能到达的城市
    can_be_reached = [set() for _ in range(N)]
    for road in roads:
        can_be_reached[road[1]-1].add(road[0]-1)
    # print(can_be_reached)

    # 从任意城市出发，能到达的城市
    can_reach_2 = [set() for _ in range(N)]
    for road in roads:
        for city in can_reach[road[0]-1]:
            can_reach_2[road[0]-1].add(city)
            can_reach_2[road[0]-1].update(can_reach[city])
    # print(can_reach_2)

    # 从任意城市出发，能到达的城市
    can_be_reached_2 = [set() for _ in range(N)]
    for road in roads:
        for city in can_be_reached[road[1]-1]:
            can_be_reached_2[road[1]-1].add(city)
            can_be_reached_2[road[1]-1].update(can_be_reached[city])
    # print(can_be_reached_2)

    # 从任意城市出发，能到达的城市
    can_reach_3 = [set() for _ in range(N)]
    for road in roads:
        for city in can_reach_2[road[0]-1]:
            can_reach_3[road[0]-1].add(city)
            can_reach_3[road[0]-1].update(can_reach_2[city])
    # print(can_reach_3)

    # 从任意城市出发，能到达的城市

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    if m == 0:
        print(n)
        return
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
    ans = 0
    for i in range(n):
        visited = [False] * n
        visited[i] = True
        stack = [i]
        while stack:
            now = stack.pop()
            for next in edge[now]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
        ans += sum(visited)
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cnt = 0
            for k in range(m):
                if a[k][0] == i and a[k][1] == j:
                    cnt += 1
            ans += cnt * cnt
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N * (N - 1) // 2 - M)

=======
Suggestion 10

def calc(n,m):
    return n*(n-1)//2
