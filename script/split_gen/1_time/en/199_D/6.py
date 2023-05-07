def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    edges = sorted(edges, key=lambda x: x[0])
    print(N, M)
    print(edges)
