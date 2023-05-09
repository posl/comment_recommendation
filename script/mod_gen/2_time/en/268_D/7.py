def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    def dfs(s):
        if len(s) == N:
            return s
        for t in S:
            if t in s:
                continue
            if dfs(s + t):
                return dfs(s + t)
        return False
    print(dfs(''))

if __name__ == '__main__':
    main()