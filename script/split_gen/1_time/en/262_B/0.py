def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) in edges:
                for k in range(j + 1, n + 1):
                    if (j, k) in edges and (k, i) in edges:
                        ans += 1
    print(ans)
