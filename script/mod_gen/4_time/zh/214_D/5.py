def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans += edges[i][2] * edges[j][2]
    print(ans)

if __name__ == '__main__':
    main()