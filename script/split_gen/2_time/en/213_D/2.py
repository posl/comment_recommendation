def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    q = [0]
    ans = []
    while q:
        v = q.pop()
        ans.append(v)
        for i in edge[v]:
            if i not in ans:
                q.append(i)
                q.append(v)
    print(*[i + 1 for i in ans])
