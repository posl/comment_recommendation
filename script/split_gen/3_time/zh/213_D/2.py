def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    for e in edge:
        e.sort()
    ans = []
    visited = [False] * n
    stack = [0]
    while stack:
        v = stack.pop()
        ans.append(v+1)
        visited[v] = True
        for e in edge[v]:
            if not visited[e]:
                stack.append(e)
    print(*ans)
