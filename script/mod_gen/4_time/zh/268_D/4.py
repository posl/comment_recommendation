def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if i != j and s[i] == s[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(m):
            if i != j and t[i] == t[j]:
                print(-1)
                return
    def dfs(i,used,ans):
        if i == n:
            print(ans)
            return True
        for j in range(m):
            if used[j]:
                continue
            if t[j].startswith(ans[-1]):
                if dfs(i+1,used[:j]+[True]+used[j+1:],ans+t[j][-1]):
                    return True
        return False
    for i in range(n):
        if dfs(1,[False]*m,s[i]):
            return

if __name__ == '__main__':
    main()