Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n,m,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    cd = [list(map(int,input().split())) for _ in range(k)]
    ans = [0]*n
    friend = [[] for _ in range(n)]
    block = [[] for _ in range(n)]
    for a,b in ab:
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    for c,d in cd:
        block[c-1].append(d-1)
        block[d-1].append(c-1)
    for i in range(n):
        ans[i] = len(set(friend[i])-set(block[i])-{i})
    print(*ans)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    relation = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        relation[a-1][b-1] = 1
        relation[b-1][a-1] = 1
    for _ in range(K):
        c, d = map(int, input().split())
        relation[c-1][d-1] = 2
        relation[d-1][c-1] = 2
    for i in range(N):
        count = 0
        for j in range(N):
            if i != j and relation[i][j] == 0:
                for k in range(N):
                    if relation[i][k] == 1 and relation[j][k] == 1:
                        count += 1
                        break
        print(count)

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    #print(N, M, K)
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    #print()
    #print()
    #print()

    #朋友候选人数
    friend_candidate = [0] * N

    #友谊关系
    friendship = []

    #阻隔关系
    blockhip = []

    #初始朋友候选人数
    for i in range(N):
        friend_candidate[i] = N - 1

    #print(friend_candidate)

    #友谊关系
    for i in range(M):
        friendship.append([A[i], B[i]])

    #阻隔关系
    for i in range(K):
        blockhip.append([C[i], D[i]])

    #print(friendship)
    #print(blockhip)

    #初始朋友候选人数
    for i in range(N):
        for j in range(M):
            if friendship[j][0] == i + 1:
                friend_candidate[i] -= 1
            if friendship[j][1] == i + 1:
                friend_candidate[i] -= 1
        for j in range(K):
            if blockhip[j][0] == i + 1:
                friend_candidate[i] -= 1
            if blockhip[j][1] == i + 1:
                friend_candidate[i] -= 1

    #print(friend_candidate)

    #朋友候选人数
    for i in range(N):
        for j in range(M):
            if friendship[j][0] == i + 1:
                for k in range(N):
                    if friend_candidate[k] == 0:
                        continue
                    if friendship[j][1] == k + 1:
                        friend_candidate[k] -= 1
            if

=======
Suggestion 4

def dfs(u, color, G):
    color[u] = 1
    for v in G[u]:
        if color[v] == 0:
            dfs(v, color, G)
    color[u] = 2

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    # 读入数据
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # 建立邻接表
    adj = [[] for _ in range(N)]
    for a, b in AB:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 建立阻隔表
    block = [[False]*N for _ in range(N)]
    for c, d in CD:
        block[c-1][d-1] = True
        block[d-1][c-1] = True
    # 计算候选人数
    for i in range(N):
        ans = 0
        for j in range(N):
            if i == j:
                continue
            if j in adj[i]:
                continue
            if block[i][j]:
                continue
            # 到这里说明j是i的候选人
            # 遍历从i到j的所有路径
            # 为了避免重复，规定只能往后走
            # 用栈实现dfs
            stack = [i]
            while stack:
                # 取出栈顶元素
                now = stack.pop()
                # 如果已经到达j，则计数+1
                if now == j:
                    ans += 1
                    break
                # 如果没到达，则将邻接点入栈
                for k in adj[now]:
                    if k in stack:
                        continue
                    stack.append(k)
        print(ans, end=' ')
    print()

=======
Suggestion 7

def input_value():
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    return N, M, K, A, B, C, D

=======
Suggestion 8

def dfs(node, visited, graph, result):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            result[i] = 1
            dfs(i, visited, graph, result)
