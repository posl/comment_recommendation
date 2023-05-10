def dfs(v, p):
    global used
    global G
    global N
    global P
    global ans
    used[v] = True
    for i in range(N):
        if G[v][i] == 1 and used[i] == False:
            dfs(i, v)
    for i in range(N):
        if G[v][i] == 1 and used[i] == True and i != p:
            P[v] = 0
            P[i] = 1
            ans += 1
N = int(input())
G = [[0 for i in range(N)] for j in range(N)]
used = [False for i in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    G[u-1][v-1] = 1
    G[v-1][u-1] = 1
P = list(map(int, input().split()))
ans = 0
dfs(0, -1)
print(ans)

if __name__ == '__main__':
    dfs()