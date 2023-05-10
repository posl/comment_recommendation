def main():
    n, m = map(int, input().split())
    ans = []
    def dfs(a):
        if len(a) == n:
            ans.append(a)
            return
        for i in range(1, m+1):
            if len(a) > 0 and i <= a[-1]:
                continue
            dfs(a + [i])
    dfs([])
    for a in ans:
        print(*a)

if __name__ == '__main__':
    main()