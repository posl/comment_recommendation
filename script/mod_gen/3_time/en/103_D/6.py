def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        visited = [False] * (N + 1)
        visited[edges[i][0]] = True
        visited[edges[i][1]] = True
        for j in range(M):
            if j == i:
                continue
            if visited[edges[j][0]] and visited[edges[j][1]]:
                continue
            visited[edges[j][0]] = True
            visited[edges[j][1]] = True
        if not all(visited):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()