Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def dfs(i, j, k):
    global ans
    if i == N:
        ans += 1
        return
    if j == 3:
        dfs(i+1, 0, k)
        return
    if k & (1 << j):
        dfs(i, j+1, k)
        return
    for x in G[i]:
        if k & (1 << C[x]):
            dfs(i, j+1, k)
            return
    C[i] = j
    dfs(i, j+1, k | (1 << j))
    C[i] = -1

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

C = [-1] * N
ans = 0
dfs(0, 0, 0)
print(ans)

=======
Suggestion 3

def dfs(v, c):
    color[v] = c
    for i in range(n):
        if G[v][i] == 0:
            continue
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

n, m = map(int, input().split())
G = [[0 for _ in range(n)] for _ in range(n)]
color = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1

=======
Suggestion 4

def solve():
    n,m = map(int,input().split())
    e = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        e[a-1].append(b-1)
        e[b-1].append(a-1)
    ans = 0
    for i in range(3**n):
        ok = True
        for j in range(n):
            for k in e[j]:
                if (i // 3**k) % 3 == (i // 3**j) % 3:
                    ok = False
        if ok:
            ans += 1
    print(ans)
solve()

=======
Suggestion 5

def dfs(i, j, k):
    if i == n:
        return 1
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    res = 0
    for l in range(3):
        if j != l and k != l:
            res += dfs(i + 1, k, l)
    dp[i][j][k] = res
    return res


n, m = map(int, input().split())
dp = [[[-1] * 3 for _ in range(3)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dp[a - 1][b - 1][0] = 0
    dp[a - 1][b - 1][1] = 0
    dp[a - 1][b - 1][2] = 0
    dp[b - 1][a - 1][0] = 0
    dp[b - 1][a - 1][1] = 0
    dp[b - 1][a - 1][2] = 0
res = 0
for i in range(3):
    for j in range(3):
        res += dfs(1, i, j)
print(res)

=======
Suggestion 6

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
color = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = 1
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            ans = 0
            break

print(ans * 3 ** color.count(0))

=======
Suggestion 7

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

N, M = map(int, input().split())
G = [[] for _ in range(N)]
color = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
        else:
            print(0)
            exit()
print(3 ** ans)

=======
Suggestion 8

def get_input():
    # 获取输入
    # 输入来自标准输入，其格式如下：
    # N M
    # A_1 B_1
    # A_2 B_2
    # A_3 B_3
    # .
    # .
    # .
    # A_M B_M
    input_line = input()
    input_line = input_line.split(" ")
    N = int(input_line[0])
    M = int(input_line[1])

    # 以字典的形式保存边的信息
    edges = {}
    for i in range(0, M):
        input_line = input()
        input_line = input_line.split(" ")
        A = int(input_line[0])
        B = int(input_line[1])
        edges[i] = [A, B]

    return N, M, edges
