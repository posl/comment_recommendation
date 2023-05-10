Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, k = map(int, input().split())
    ab = []
    cd = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    for i in range(k):
        cd.append(list(map(int, input().split())))
    #print(n, m, k)
    #print(ab)
    #print(cd)
    #print()

=======
Suggestion 2

def solve():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blocks[c].append(d)
        blocks[d].append(c)
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(friends[i]) - set(friends[i]) & set(blocks[i]) - {i}) - 1
    print(*ans)

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        ai, bi = map(int, input().split())
        a[ai - 1] += 1
        b[bi - 1] += 1
    c = [0] * n
    d = [0] * n
    for i in range(k):
        ci, di = map(int, input().split())
        c[ci - 1] += 1
        d[di - 1] += 1
    for i in range(n):
        print(a[i] - c[i] - 1, end=' ')
    print()

=======
Suggestion 4

def make_set(x):
    p[x] = x
    rank[x] = 0

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    friend = [[] for _ in range(N)]
    block = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friend[A - 1].append(B - 1)
        friend[B - 1].append(A - 1)
    for _ in range(K):
        C, D = map(int, input().split())
        block[C - 1].append(D - 1)
        block[D - 1].append(C - 1)
    for i in range(N):
        friend[i] = set(friend[i])
        block[i] = set(block[i])
    for i in range(N):
        print(len(friend[i] - block[i] - {i}) - 1, end=" ")
    print()

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    # 人iと人jの友達関係をグラフで表す
    friend = [[] for _ in range(N)]
    for A, B in AB:
        friend[A-1].append(B-1)
        friend[B-1].append(A-1)

    # 人iと人jのブロック関係をグラフで表す
    block = [[] for _ in range(N)]
    for C, D in CD:
        block[C-1].append(D-1)
        block[D-1].append(C-1)

    # 人iの友達候補の数を求める
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(friend[i]) - set(friend[i]) & set(block[i]) - {i} - set(friend[i]))

    print(*ans)

=======
Suggestion 7

def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)

n,m,k=map(int,input().split())
graph=[[] for _ in range(n)]
visited=[False]*n

for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

for _ in range(k):
    c,d=map(int,input().split())
    c-=1
    d-=1
    graph[c].append(d)
    graph[d].append(c)

for i in range(n):
    if visited[i]:
        continue
    dfs(i)

ans=[0]*n
for i in range(n):
    for j in graph[i]:
        if visited[j]:
            continue
        ans[i]+=1

print(*ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    friends = []
    blocks = []
    for i in range(M):
        friends.append(list(map(int, input().split())))
    for i in range(K):
        blocks.append(list(map(int, input().split())))
    # print(friends)
    # print(blocks)
    # 人と人の友達候補の数を格納するリスト
    ans = [0] * N
    # 人と人の友達候補の数を格納するリスト
    # ans = [0 for i in range(N)]
    # print(ans)
    # 人と人の友達関係を格納するリスト
    friends_list = [[] for i in range(N)]
    # 人と人のブロック関係を格納するリスト
    blocks_list = [[] for i in range(N)]
    # print(friends_list)
    # print(blocks_list)
    # 友達関係
    for i in range(M):
        # 友達関係の人を格納
        friends_list[friends[i][0] - 1].append(friends[i][1] - 1)
        friends_list[friends[i][1] - 1].append(friends[i][0] - 1)
    # print(friends_list)
    # ブロック関係
    for i in range(K):
        # ブロック関係の人を格納
        blocks_list[blocks[i][0] - 1].append(blocks[i][1] - 1)
        blocks_list[blocks[i][1] - 1].append(blocks[i][0] - 1)
    # print(blocks_list)
    # 人と人の友達候補の数を格納
    for i in range(N):
        # 人と人の友達候補の数を格納
        ans[i] = N - len(friends_list[i]) - len(blocks_list[i]) - 1
        # 人と人の友達関係を格納
        for j in friends_list[i]:
            # 人と人の

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    friend = [[] for _ in range(N)]
    block = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        block[c-1].append(d-1)
        block[d-1].append(c-1)
    ans = [0]*N
    for i in range(N):
        ans[i] = len(set(friend[i]) - set(friend[i]) & set(block[i])) - 1
    print(*ans)

=======
Suggestion 10

def solve():
    from sys import stdin
    readline = stdin.readline
    N, M, K = map(int, readline().split())
    friends = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        friends[a].add(b)
        friends[b].add(a)
    for _ in range(K):
        c, d = map(int, readline().split())
        c -= 1
        d -= 1
        blocks[c].add(d)
        blocks[d].add(c)

    # dfs
    def dfs(v, seen):
        seen.add(v)
        for u in friends[v]:
            if u not in seen and u not in blocks[v]:
                dfs(u, seen)
        return seen

    ans = [0] * N
    for i in range(N):
        ans[i] = len(dfs(i, set())) - len(friends[i]) - 1
    print(*ans)
