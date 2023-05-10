def main():
    n = int(input())
    edges = []
    for _ in range(n):
        u, v = map(int, input().split())
        edges.append((u, v))
    pieces = list(map(int, input().split()))
    print(solve(n, edges, pieces))
