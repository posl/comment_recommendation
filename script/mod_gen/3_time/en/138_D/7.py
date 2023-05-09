def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    ops = [list(map(int, input().split())) for _ in range(Q)]
    edges.sort(key=lambda x: x[1])
    tree = [[] for _ in range(N+1)]
    for edge in edges:
        tree[edge[0]].append(edge[1])
    scores = [0] * (N+1)
    for op in ops:
        scores[op[0]] += op[1]
    for i in range(1, N+1):
        for j in tree[i]:
            scores[j] += scores[i]
    print(*scores[1:])

if __name__ == '__main__':
    main()