def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    def dfs(v, t):
        if len(v) == N:
            if t == K:
                return 1
            else:
                return 0
        else:
            res = 0
            for i in range(N):
                if i not in v:
                    res += dfs(v + [i], t + T[v[-1]][i])
            return res
    print(dfs([0], 0))
