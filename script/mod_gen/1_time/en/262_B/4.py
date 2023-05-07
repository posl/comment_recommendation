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
            w, x = edges[j]
            if u == w or u == x or v == w or v == x:
                continue
            if (u, v) in edges and (v, w) in edges and (w, u) in edges:
                ans += 1
            if (u, v) in edges and (v, x) in edges and (x, u) in edges:
                ans += 1
            if (u, w) in edges and (w, v) in edges and (v, u) in edges:
                ans += 1
            if (u, w) in edges and (w, x) in edges and (x, u) in edges:
                ans += 1
            if (u, x) in edges and (x, v) in edges and (v, u) in edges:
                ans += 1
            if (u, x) in edges and (x, w) in edges and (w, u) in edges:
                ans += 1
            if (v, w) in edges and (w, u) in edges and (u, v) in edges:
                ans += 1
            if (v, w) in edges and (w, x) in edges and (x, v) in edges:
                ans += 1
            if (v, x) in edges and (x, u) in edges and (u, v) in edges:
                ans += 1
            if (v, x) in edges and (x, w) in edges and (w, v) in edges:
                ans += 1
            if (w, x) in edges and (x, u) in edges and (u, w) in edges:
                ans += 1
            if (w, x) in edges and (x, v) in edges and (v, w) in edges:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()