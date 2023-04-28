Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    friends = [[] for _ in range(N+1)]
    blocks = [[] for _ in range(N+1)]
    for a, b in AB:
        friends[a].append(b)
        friends[b].append(a)
    for c, d in CD:
        blocks[c].append(d)
        blocks[d].append(c)

    ans = [0] * (N+1)
    for i in range(1, N+1):
        ans[i] = len(set(friends[i]) & set(friends[i]) - set(blocks[i]) - {i}) - len(set(friends[i]) & set(blocks[i]))

    print(*ans[1:])

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    # 人iの友達の数
    friends = [0] * (N + 1)

    # 人iのブロックの数
    blocks = [0] * (N + 1)

    for a, b in AB:
        friends[a] += 1
        friends[b] += 1

    for c, d in CD:
        blocks[c] += 1
        blocks[d] += 1

    result = [0] * (N + 1)
    for i in range(1, N + 1):
        result[i] = friends[i] - blocks[i] - 1

    print(*result[1:])

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    cd = [list(map(int, input().split())) for _ in range(k)]

    friend = [0] * (n + 1)
    block = [0] * (n + 1)
    for a, b in ab:
        friend[a] += 1
        friend[b] += 1
    for c, d in cd:
        block[c] += 1
        block[d] += 1

    for i in range(1, n + 1):
        print(friend[i] - block[i] - 1, end=" ")

=======
Suggestion 4

def main():
    n, m, k = map(int, input().split())
    friend = [set() for _ in range(n)]
    block = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a-1].add(b-1)
        friend[b-1].add(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        block[c-1].add(d-1)
        block[d-1].add(c-1)
    ans = [0] * n
    for i in range(n):
        ans[i] = len(friend[i] - block[i] - {i})
    print(*ans)

main()

=======
Suggestion 5

def dfs(v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

N, M, K = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
color = [0] * N
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print(0)
            exit()
ans = [0] * N
for i in range(N):
    ans[i] = color.count(color[i])
for i in range(N):
    ans[i] -= len(G[i]) + 1
print(*ans)

=======
Suggestion 6

def main():
    n,m,k = map(int,input().split())
    friend = [set() for _ in range(n)]
    block = [set() for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        friend[a-1].add(b-1)
        friend[b-1].add(a-1)
    for _ in range(k):
        c,d = map(int,input().split())
        block[c-1].add(d-1)
        block[d-1].add(c-1)
    ans = [0]*n
    for i in range(n):
        ans[i] = len(friend[i]-block[i]-{i})  #自分自身を除く
    print(*ans)

=======
Suggestion 7

def main():
    # 入力
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    
    # 友達候補数
    ans = [0] * N
    
    # 友達関係を表すグラフ
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    # ブロック関係を表すグラフ
    B = [[] for _ in range(N)]
    for c, d in CD:
        B[c - 1].append(d - 1)
        B[d - 1].append(c - 1)
    
    # 各人の友達候補数を求める
    for i in range(N):
        # 自分自身は除外
        ans[i] = len(set(G[i]) - set(B[i])) - 1
    
    # 出力
    print(*ans)

=======
Suggestion 8

def main():
    n,m,k = map(int,input().split())
    ab = [list(map(int,input().split())) for i in range(m)]
    cd = [list(map(int,input().split())) for i in range(k)]

    #友達関係のグラフを作る
    friend = [[] for i in range(n)]
    for i in range(m):
        a,b = ab[i][0],ab[i][1]
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)

    #ブロック関係のグラフを作る
    block = [[] for i in range(n)]
    for i in range(k):
        c,d = cd[i][0],cd[i][1]
        block[c-1].append(d-1)
        block[d-1].append(c-1)

    #友達候補の数を求める
    for i in range(n):
        ans = len(friend[i]) - 1
        for j in friend[i]:
            if j in block[i]:
                ans -= 1
        print(ans,end=" ")

=======
Suggestion 9

def dfs(v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and not dfs(graph[v][i], -c):
            return False
    return True

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print(0)
            exit()

ans = [0] * n
for i in range(n):
    ans[i] = graph[i].count(-1) + 1

print(*ans)

=======
Suggestion 10

def dfs(v, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == c:
            return False
        if color[g[v][i]] == 0 and not dfs(g[v][i], -c):
            return False
    return True

n, m, k = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
color = [0 for i in range(n)]
for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print(-1)
            exit()
ans = [0 for i in range(n)]
for i in range(n):
    ans[i] = len(g[i])
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        ans[c] -= 1
        ans[d] -= 1
print(*ans)
