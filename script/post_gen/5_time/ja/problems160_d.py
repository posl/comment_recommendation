Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X,Y = map(int,input().split())

    ans = [0] * N

    for i in range(1,N):
        for j in range(i+1,N+1):
            d = min(j-i,abs(X-i)+1+abs(Y-j))
            ans[d] += 1

    for i in range(1,N):
        print(ans[i])

=======
Suggestion 2

def getDistance(start, goal, n):
    if start == goal:
        return 0
    if start > goal:
        start, goal = goal, start
    if start == 1 and goal == n:
        return 1
    if start == 1:
        return goal - start
    if goal == n:
        return goal - start
    return min(goal - start, start + n - goal)

=======
Suggestion 3

def main():
    n,x,y = map(int, input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans[min(j-i,abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(ans[i])

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-1):
        graph[i][i+1] = 1
        graph[i+1][i] = 1
    graph[X-1][Y-1] = 1
    graph[Y-1][X-1] = 1
    for k in range(N-1):
        for i in range(N-1):
            for j in range(i+1, N):
                if graph[i][j] == 0 and graph[i][k] != 0 and graph[k][j] != 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    graph[j][i] = graph[i][j]
    for i in range(N-1):
        count = 0
        for j in range(i+1, N):
            if graph[i][j] != 0:
                count += 1
        print(count)
    return

=======
Suggestion 5

def main():
    n,x,y = map(int,input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            d = min(j-i,abs(i-x)+abs(j-y)+1)
            ans[d-1] += 1
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[d] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            ans[min(j - i, abs(X - i) + 1 + abs(Y - j))] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 8

def bfs():
    # 未探索の頂点を格納するスタック
    stack = []
    # 未探索の頂点をスタックに追加
    stack.append(1)
    # 未探索の頂点がなくなるまで繰り返す
    while len(stack) > 0:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点 v に隣接する頂点を全て調べる
        for i in range(len(g[v])):
            # 隣接する頂点が未探索の場合はスタックに追加
            if d[g[v][i]] == -1:
                # 頂点 g[v][i] に隣接する頂点をスタックに追加
                stack.append(g[v][i])
                # 頂点 g[v][i] に隣接する頂点の距離を更新
                d[g[v][i]] = d[v] + 1

n,x,y = map(int,input().split())
g = [[] for _ in range(n+1)]
for i in range(1,n):
    g[i].append(i+1)
    g[i+1].append(i)
g[x].append(y)
g[y].append(x)
d = [-1]*(n+1)
d[1] = 0
bfs()
for i in range(1,n):
    ans = 0
    for j in range(i+1,n+1):
        ans += d[j].count(i)
    print(ans)

=======
Suggestion 9

def solve():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    ans = [0]*(N-1)
    for i in range(N):
        for j in range(i+1,N):
            d = min(j-i,abs(X-i)+1+abs(Y-j))
            ans[d-1] += 1
    return ans

=======
Suggestion 10

def main():
    n,x,y = map(int,input().split())
    ans = [0] * n
    for i in range(1,n):
        for j in range(i+1,n+1):
            #print("i:",i,"j:",j)
            k = min(j-i,abs(x-i)+abs(y-j)+1)
            #print("k:",k)
            ans[k] += 1
    for i in range(1,n):
        print(ans[i])
