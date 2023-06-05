def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort()
    ans = 0
    for i in range(m):
        u, v = edges[i]
        if i == 0 or edges[i - 1] != (u, v):
            ans += 1
    print(ans)
