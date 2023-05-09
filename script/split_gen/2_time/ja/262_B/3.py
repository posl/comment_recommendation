def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    ans = 0
    for i in range(n):
        for j in graph[i]:
            for k in graph[j]:
                if i == k:
                    ans += 1
    print(ans // 6)
