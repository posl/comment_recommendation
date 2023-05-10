def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    def check(x):
        for i in range(m):
            if t[i] in x:
                return False
        return True
    def dfs(x):
        if len(x) == n:
            if check(x):
                print(x)
                exit()
            return
        for i in range(n):
            dfs(x + s[i])
    dfs("")

if __name__ == '__main__':
    main()