def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    def check(x):
        for t in T:
            if t in x:
                return False
        return True
    def dfs(i, x):
        if i == N:
            if check(x):
                print(x)
                exit()
            return
        for j in range(1, 16):
            dfs(i+1, x + "_" * j + S[i])
    dfs(0, "")
    print(-1)
