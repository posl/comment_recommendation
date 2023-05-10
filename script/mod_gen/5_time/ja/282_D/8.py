def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    color = [-1]*n
    def dfs(v,c):
        color[v] = c
        for i in g[v]:
            if color[i] == c:
                return False
            if color[i] == -1 and not dfs(i,1-c):
                return False
        return True
    ans = 0
    for i in range(n):
        if color[i] == -1:
            if dfs(i,1):
                ans += 1
    print(ans*(ans-1)//2-m+ans)
main()

if __name__ == '__main__':
    main()