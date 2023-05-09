def main():
    n,k = map(int,input().split())
    t = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    def dfs(i,visited):
        if len(visited) == n:
            if sum(t[i][0] for i in visited) == k:
                nonlocal ans
                ans += 1
            return
        for j in range(n):
            if j not in visited:
                dfs(j,visited+[j])
    dfs(0,[0])
    print(ans)
