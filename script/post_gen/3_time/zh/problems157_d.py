Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,m,k = map(int,input().split())
    friends = [set() for i in range(n)]
    blocks = [set() for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    for i in range(k):
        c,d = map(int,input().split())
        blocks[c-1].add(d-1)
        blocks[d-1].add(c-1)
    for i in range(n):
        print(len(friends[i] - blocks[i] - {i}),end=' ')
    print()

=======
Suggestion 3

def get_input():
    n, m, k = map(int, input().split())
    friends = []
    blocks = []
    for i in range(m):
        friends.append(list(map(int, input().split())))
    for i in range(k):
        blocks.append(list(map(int, input().split())))
    return n, m, k, friends, blocks

=======
Suggestion 4

def solve(n, m, k, a, b, c, d):
    # 1. 求出所有的朋友关系
    friends = [[] for _ in range(n + 1)]
    for i in range(m):
        friends[a[i]].append(b[i])
        friends[b[i]].append(a[i])
    # 2. 求出所有的阻隔关系
    blocks = [[] for _ in range(n + 1)]
    for i in range(k):
        blocks[c[i]].append(d[i])
        blocks[d[i]].append(c[i])
    # 3. 求出所有的候选人
    candidates = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and j not in friends[i] and j not in blocks[i]:
                candidates[i].append(j)
    # 4. 求出每个用户的候选人数
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = len(candidates[i])
    return ans[1:]

=======
Suggestion 5

def dfs(now, goal, visited, friends, blocks):
    if now == goal:
        return True
    visited[now] = True
    for friend in friends[now]:
        if not visited[friend]:
            if dfs(friend, goal, visited, friends, blocks):
                return True
    return False

N, M, K = map(int, input().split())
friends = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    friends[A - 1].append(B - 1)
    friends[B - 1].append(A - 1)

blocks = [[] for _ in range(N)]
for _ in range(K):
    C, D = map(int, input().split())
    blocks[C - 1].append(D - 1)
    blocks[D - 1].append(C - 1)

for i in range(N):
    visited = [False] * N
    ans = 0
    for j in range(N):
        if i == j:
            continue
        if not dfs(i, j, visited, friends, blocks):
            ans += 1
    print(ans, end=' ')

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)

    blocks = [[] for _ in range(N)]
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)

    candidate = [0] * N
    for i in range(N):
        for j in friends[i]:
            candidate[i] += 1
        for j in blocks[i]:
            candidate[i] -= 1
        candidate[i] -= 1
    print(" ".join(map(str, candidate)))

=======
Suggestion 7

def main():
    n,m,k = map(int,input().split())
    a = [0] * m
    b = [0] * m
    c = [0] * k
    d = [0] * k
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(k):
        c[i],d[i] = map(int,input().split())
    print(a,b,c,d)
    for i in range(1,n+1):
        cnt = 0
        for j in range(m):
            if a[j] == i:
                cnt += 1
            if b[j] == i:
                cnt += 1
        for j in range(k):
            if c[j] == i:
                cnt -= 1
            if d[j] == i:
                cnt -= 1
        print(cnt,end=' ')
    print()
