def main():
    n = int(input())
    edge = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edge.append((w, u, v))
    edge.sort()
    ans = 0
    for i in range(n-1):
        ans += edge[i][0] * (i+1) * (n-i-1)
    print(ans)
