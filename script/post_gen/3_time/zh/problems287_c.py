Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def isPathGraph(num, edges):
    for i in range(1, num+1):
        if len(edges[i]) != 2:
            return "No"
    return "Yes"

=======
Suggestion 3

def main():
    # 读入数据
    n, m = map(int, input().split())
    # 生成邻接表
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    # 判断是否为路径图
    for u in range(n):
        if len(adj[u]) > 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    for i in range(N):
        G[i].sort()
    for i in range(N):
        if len(G[i]) == 2:
            continue
        if len(G[i]) == 0:
            print("No")
            return
        if len(G[i]) == 1:
            if len(G[G[i][0]]) == 1:
                print("No")
                return
    print("Yes")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    edge = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u][v] = 1
        edge[v][u] = 1
    for i in range(n):
        for j in range(i + 1, n):
            if edge[i][j] == 1:
                for k in range(j + 1, n):
                    if edge[i][k] == 1 and edge[j][k] == 1:
                        print('No')
                        return
    print('Yes')
    return

=======
Suggestion 6

def main():
    # 读取输入
    n, m = map(int, input().split())
    # 邻接表
    adj = [[] for _ in range(n)]
    # 读取边
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    # 判断
    for i in range(n):
        if len(adj[i]) > 2:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    print(A)
    print(N)
    print(M)
    print(A[0][0])
    print(A[0][1])
    print(A[1][0])
    print(A[1][1])
    print(A[2][0])
    print(A[2][1])
    print(A[3][0])
    print(A[3][1])
    print(A[4][0])
    print(A[4][1])
    print(A[5][0])
    print(A[5][1])
    print(A[6][0])
    print(A[6][1])
    print(A[7][0])
    print(A[7][1])
    print(A[8][0])
    print(A[8][1])
    print(A[9][0])
    print(A[9][1])
    print(A[10][0])
    print(A[10][1])
    print(A[11][0])
    print(A[11][1])
    print(A[12][0])
    print(A[12][1])
    print(A[13][0])
    print(A[13][1])
    print(A[14][0])
    print(A[14][1])
    print(A[15][0])
    print(A[15][1])
    print(A[16][0])
    print(A[16][1])
    print(A[17][0])
    print(A[17][1])
    print(A[18][0])
    print(A[18][1])
    print(A[19][0])
    print(A[19][1])
    print(A[20][0])
    print(A[20][1])
    print(A[21][0])
    print(A[21][1])
    print(A[22][0])
    print(A[22][1])
    print(A[23][0])
    print(A[23][1])
    print(A[24][0])
    print(A[24][1])
    print(A[25][0])
    print(A[25][1])
    print(A[26][0])
    print(A[26][1])
    print(A[27][0])
    print(A[27][1])
    print(A[28][0])

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())

    # 1. 无向图
    for i in range(M):
        u[i] -= 1
        v[i] -= 1

    # 2. N个顶点
    if N != len(set(u + v)):
        print("No")
        return

    # 3. N-1条边
    if M != N - 1:
        print("No")
        return

    # 4. 一个序列
    if M != len(set(u + v)):
        print("No")
        return

    # 5. 1~N的排列组合
    if set(u + v) != set(range(N)):
        print("No")
        return

    # 6. 满足条件
    for i in range(M):
        if abs(u[i] - v[i]) != 1:
            print("No")
            return

    print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))

    # print(edges)
    # print(N, M)

    # 1.如果有自循环或多条边，不是简单无向图
    # 2.如果有方向，不是简单无向图
    # 3.如果有环，不是简单无向图
    # 4.如果有孤立点，不是路径图
    # 5.如果有度为2的点，不是路径图
    # 6.如果有度为1的点，不是路径图
    # 7.如果有度为0的点，不是路径图

    # 1.如果有自循环或多条边，不是简单无向图
    # 2.如果有方向，不是简单无向图
    # 3.如果有环，不是简单无向图
    # 4.如果有孤立点，不是路径图
    # 5.如果有度为2的点，不是路径图
    # 6.如果有度为1的点，不是路径图
    # 7.如果有度为0的点，不是路径图
    if M != N - 1:
        print('No')
        return

    # 1.如果有自循环或多条边，不是简单无向图
    # 2.如果有方向，不是简单无向图
    # 3.如果有环，不是简单无向图
    # 4.如果有孤立点，不是路径图
    # 5.如果有度为2的点，不是路径图
    # 6.如果有度为1的点，不是路径图
    # 7.如果有度为0的点，不是路径图
    # 1.如果有自循环或多条边，不是简单无向图
    # 2.如果有方
