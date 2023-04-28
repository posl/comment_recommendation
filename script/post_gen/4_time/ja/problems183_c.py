Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += dfs(i, 1 << i, K - T[0][i], N, T)
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, n):
        ans += dfs(i, 1 << i, 1, n, k, t)
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if t[i][j] + t[j][i] == k:
                ans += 1
    print(ans//2)

=======
Suggestion 4

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

=======
Suggestion 5

def dfs(now, visited, cost):
    if now == 0:
        return cost == k
    visited[now] = True
    ret = 0
    for i in range(n):
        if not visited[i]:
            ret += dfs(i, visited, cost + t[now][i])
    visited[now] = False
    return ret

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
print(dfs(0, visited, 0))

=======
Suggestion 6

def dfs(now, visited, cost, n, k, t):
    visited[now] = True
    if all(visited):
        return cost + t[now][0] == k
    else:
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += dfs(i, visited, cost + t[now][i], n, k, t)
        return ans

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
print(dfs(0, visited, 0, n, k, t))

=======
Suggestion 7

def dfs(city, time, visited, n):
    if len(visited) == n:
        return 1 if time == k else 0
    ret = 0
    for i in range(1, n):
        if not i in visited:
            ret += dfs(i, time+t[city][i], visited+[i], n)
    return ret

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, 0, [0], n))

=======
Suggestion 8

def dfs(now,visited):
    if visited==2**n-1:
        if now==0:
            return 1
        else:
            return 0
    elif now in dp and visited in dp[now]:
        return dp[now][visited]
    else:
        ans=0
        for i in range(n):
            if visited>>i&1==0:
                ans+=dfs(i,visited|1<<i)
        if now in dp:
            dp[now][visited]=ans
        else:
            dp[now]={visited:ans}
        return ans

n,k=map(int,input().split())
t=[list(map(int,input().split())) for i in range(n)]
dp={}
print(dfs(0,1))

=======
Suggestion 9

def main():
    pass
