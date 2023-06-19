def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort()
    # print(edges)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            u1, v1 = edges[i]
            u2, v2 = edges[j]
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()