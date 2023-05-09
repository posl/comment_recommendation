def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort()
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if edges[i][0] < edges[j][0] and edges[i][1] < edges[j][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()