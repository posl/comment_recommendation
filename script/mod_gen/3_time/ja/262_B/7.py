def main():
    N, M = map(int, input().split())
    #辺のリスト
    edges = []
    #頂点のリスト
    nodes = []
    #頂点の次数のリスト
    degrees = [0 for i in range(N)]
    #頂点の次数のリスト
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    #次数が2以上の頂点をnodesに追加
    for i in range(N):
        if degrees[i] >= 2:
            nodes.append(i + 1)
    #nodesの要素の組み合わせを全て試す
    ans = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                if (nodes[i], nodes[j]) in edges and (nodes[j], nodes[k]) in edges and (nodes[k], nodes[i]) in edges:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()