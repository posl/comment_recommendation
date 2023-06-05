def main():
    n, m = map(int, input().split())
    edge = []
    for i in range(m):
        u, v = map(int, input().split())
        edge.append((u, v))
    ans = 0
    for i in range(m):
        u, v = edge[i]
        for j in range(i + 1, m):
            if edge[j][0] == u or edge[j][0] == v or edge[j][1] == u or edge[j][1] == v:
                continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()