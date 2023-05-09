def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    def dfs(v, c):
        if len(c) == N:
            return 1 if v == 0 and sum(c) == K else 0
        return sum(dfs(i, c + [T[v][i]]) for i in range(N) if i not in c)
    print(dfs(0, []))

if __name__ == '__main__':
    main()