Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    #print(n,m)
    #print(n)
    #print(m)
    #pr

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(N)
    #print(M)
    #print(A)
    #print(B)
    #print(N)
    #p

=======
Suggestion 3

def find_way(from_city, to_city, roads):
    if from_city == to_city:
        return 0

    min_time = 0
    for road in roads:
        if road[0] == from_city:
            next_city = road[1]
            time = find_way(next_city, to_city, roads)
            if time != 0:
                if min_time == 0 or min_time > time + 1:
                    min_time = time + 1

    return min_time

=======
Suggestion 4

def main():
    N,M=map(int,input().split())
    A=[0]*M
    B=[0]*M
    for i in range(M):
        A[i],B[i]=map(int,input().split())
    print(N,M,A,B)
    return 0

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M, A, B)
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N, M, A, B)
    return

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]
    print(A, B)
    print(N, M)
    pass

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    # 邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 队列
    q = [0]
    # 距离
    dist = [0]+[float('inf')]*(n-1)
    # 记录路径条数
    cnt = [0]*n
    cnt[0] = 1
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u]+1
                q.append(v)
                cnt[v] = cnt[u]
            elif dist[v] == dist[u]+1:
                cnt[v] += cnt[u]
    print(cnt[-1] % (10**9+7))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        if a == 1:
            s[b] = 1
        elif b == n:
            s[a] = 1
    ans = 0
    for i in range(2, n):
        if s[i] == 1 and s[i + 1] == 1:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[1])
    #print(AB)
    ans = 1
    max_v = AB[0][1]
    for i in range(1, M):
        if AB[i][0] >= max_v:
            max_v = AB[i][1]
            ans += 1
    print(ans)
