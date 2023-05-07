def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    def dfs(v, k):
        if k == N - 1:
            return T[v][0]
        res = 0
        for i in range(N):
            if i != v and not used[i]:
                used[i] = True
                res += dfs(i, k + 1)
                used[i] = False
        return res
    used = [False] * N
    used[0] = True
    print(dfs(0, 0))
