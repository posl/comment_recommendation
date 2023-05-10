def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort(key=lambda x: x[0])
    ans = 0
    cur = 0
    for i in range(1, n + 1):
        if edges[cur][0] == i:
            cur += 1
        else:
            ans += n - i
    print(ans)
