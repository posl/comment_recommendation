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
