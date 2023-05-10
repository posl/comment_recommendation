def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    print(edges)
