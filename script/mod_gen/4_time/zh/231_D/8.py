def dfs(i):
    visited[i] = 1
    for j in G[i]:
        if visited[j] == 1:
            return False
        elif visited[j] == 0:
            if not dfs(j):
                return False
    visited[i] = 2
    return True
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
visited = [0] * N
for i in range(N):
    if visited[i] == 0:
        if not dfs(i):
            print("No")
            exit()
print("Yes")

if __name__ == '__main__':
    dfs()