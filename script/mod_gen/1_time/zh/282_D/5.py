def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edge = list(map(int, input().split()))
        edges.append(edge)
    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            if edges[i][0] != edges[j][0] and edges[i][0] != edges[j][1] and edges[i][1] != edges[j][0] and edges[i][1] != edges[j][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()