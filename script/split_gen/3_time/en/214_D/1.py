def main():
    N = int(input())
    edges = []
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))
    ans = 0
    for u, v, w in edges:
        ans += w * (N - 1)
    print(ans)
