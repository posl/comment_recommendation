def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        A, B = map(int, input().split())
        edges.append((A, B))
    print(edges)
