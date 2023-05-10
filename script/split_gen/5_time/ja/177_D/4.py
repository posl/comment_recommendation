def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [False] * n
    ans = 0
    for i in range(n):
        if visited[i]:
            continue
        ans += 1
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for nv in graph[v]:
                if visited[nv]:
                    continue
                visited[nv] = True
                stack.append(nv)
    print(ans)
