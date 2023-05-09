def main():
    N, M = map(int, input().split())
    edges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)
    for i in range(N):
        print(len(edges[i]), end=' ')
        for j in sorted(edges[i]):
            print(j + 1, end=' ')
        print()
