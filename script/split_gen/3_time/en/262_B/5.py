def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))
    count = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    count += 1
    print(count)
