def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    ans = 0
    for i in range(M):
        u, v = edges[i]
        for j in range(i+1, M):
            x, y = edges[j]
            if u == x or u == y or v == x or v == y:
                continue
            if (u, v) not in edges and (v, u) not in edges:
                continue
            if (x, y) not in edges and (y, x) not in edges:
                continue
            if (u, x) in edges or (x, u) in edges:
                if (v, y) in edges or (y, v) in edges:
                    ans += 1
            if (u, y) in edges or (y, u) in edges:
                if (v, x) in edges or (x, v) in edges:
                    ans += 1
    print(ans)
