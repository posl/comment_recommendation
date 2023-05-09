def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((v - 1, w))
        edge[v - 1].append((u - 1, w))
    ans = 0
    for i in range(n):
        for j, w in edge[i]:
            ans += w * (n - 1) * 2
    print(ans)

if __name__ == '__main__':
    main()