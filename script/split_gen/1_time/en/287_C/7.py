def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    if M == 0:
        print('Yes')
        return
    if M != N - 1:
        print('No')
        return
    nodes = [0] * (N + 1)
    for u, v in edges:
        nodes[u] += 1
        nodes[v] += 1
    print('Yes' if all(n == 2 for n in nodes) else 'No')
