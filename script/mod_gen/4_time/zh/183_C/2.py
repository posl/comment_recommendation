def main():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    # print(T)
    # print(len(T))
    # 递归函数
    def dfs(i, j, t, visited):
        visited = visited[:]
        visited.append(j)
        if len(visited) == N:
            if t + T[i][j] == K:
                return 1
            else:
                return 0
        else:
            ans = 0
            for k in range(N):
                if k not in visited:
                    ans += dfs(j, k, t + T[i][j], visited)
            return ans
    ans = 0
    for i in range(N):
        ans += dfs(i, i, 0, [])
    print(ans)

if __name__ == '__main__':
    main()