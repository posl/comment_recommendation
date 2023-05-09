def main():
    N, M = map(int, input().split())
    if N == 2:
        print(0)
        return
    if M == 0:
        print(0)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[AB[i][0]-1].append(AB[i][1]-1)
        adj[AB[i][1]-1].append(AB[i][0]-1)
    #print(adj)
    visited = [0] * N
    visited[0] = 1
    count = [0] * N
    count[0] = 1
    stack = [0]
    while len(stack) > 0:
        u = stack.pop()
        for v in adj[u]:
            if visited[v] == 0:
                visited[v] = 1
                count[v] = count[u]
                stack.append(v)
            elif visited[v] == 1:
                count[v] += count[u]
    print(count[N-1]%(10**9+7))
