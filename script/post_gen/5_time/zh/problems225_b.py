Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    # 初始化
    d = [0 for i in range(N)]
    # 统计
    for i in range(N-1):
        d[a[i]-1] += 1
        d[b[i]-1] += 1
    # 判断
    if max(d) == N-1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    #print(edges)
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[0][0] == 1)
    #print(edges[0][1] == 1)
    #print(edges[0][0] == 2)
    #print(edges[0][1] == 2)
    #print(edges[0][0] == 3)
    #print(edges[0][1] == 3)
    #print(edges[0][0] == 4)
    #print(edges[0][1] == 4)
    #print(edges[0][0] == 5)
    #print(edges[0][1] == 5)
    #print(edges[0][0] == 6)
    #print(edges[0][1] == 6)
    #print(edges[0][0] == 7)
    #print(edges[0][1] == 7)
    #print(edges[0][0] == 8)
    #print(edges[0][1] == 8)
    #print(edges[0][0] == 9)
    #print(edges[0][1] == 9)
    #print(edges[0][0] == 10)
    #print(edges[0][1] == 10)
    #print(edges[0][0] == 11)
    #print(edges[0][1] == 11)
    #print(edges[0][0] == 12)
    #print(edges[0][1] == 12)
    #print(edges[0][0] == 13)
    #print(edges[0][1] == 13)
    #print(edges[0][0] == 14)
    #print(edges[0][1] == 14)
    #print(edges[0][0] == 15)
    #print(edges[0][1] == 15)
    #print(edges[0][0] == 16)
    #print(edges[0][1] == 16)
    #print(edges[0][0] == 17)
    #print(edges[0][1] == 17)
    #print

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if a[0] == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    # 读入数据
    N = int(input())
    a = []
    b = []
    for _ in range(N-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # 生成邻接表
    adj = [[] for _ in range(N+1)]
    for i in range(N-1):
        adj[a[i]].append(b[i])
        adj[b[i]].append(a[i])

    # 判断是否是星形
    for i in range(1, N+1):
        if len(adj[i]) == N-1:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def problems225_b():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    nodes = {}
    for i in range(n-1):
        a,b = map(int,input().split())
        nodes[a] = nodes.get(a,0)+1
        nodes[b] = nodes.get(b,0)+1
    if max(nodes.values()) == n-1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_star(n,ab):
    a,b = [list(i) for i in zip(*ab)]
    a = [i-1 for i in a]
    b = [i-1 for i in b]
    c = [0]*n
    for i in a:
        c[i] += 1
    for i in b:
        c[i] += 1
    if max(c) == n-1 and min(c) == 1:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    n = int(input())
    ab = []
    for i in range(n-1):
        ab.append(list(map(int, input().split())))
    ab.sort()
    #print(ab)
    a = [0] * n
    for i in range(n-1):
        a[ab[i][0]-1] += 1
    #print(a)
    for i in range(n-1):
        if a[ab[i][1]-1] == n-1:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def main():
    N = int(input())
    A = [0] * (N - 1)
    B = [0] * (N - 1)
    for i in range(N - 1):
        A[i], B[i] = map(int, input().split())
    # 每个顶点的度数
    degree = [0] * N
    for i in range(N - 1):
        degree[A[i] - 1] += 1
        degree[B[i] - 1] += 1
    # 找到度数为N-1的顶点
    for i in range(N):
        if degree[i] == N - 1:
            print("Yes")
            return
    print("No")
    return
