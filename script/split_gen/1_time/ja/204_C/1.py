def main():
    N,M = map(int,input().split())
    graph = [[] for i in range(N+1)]
    for i in range(M):
        A,B = map(int,input().split())
        graph[A].append(B)
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                visited = [0 for i in range(N+1)]
                visited[i] = 1
                stack = [i]
                while stack:
                    v = stack.pop()
                    if v == j:
                        ans += 1
                        break
                    for nv in graph[v]:
                        if visited[nv] == 0:
                            visited[nv] = 1
                            stack.append(nv)
    print(ans)
