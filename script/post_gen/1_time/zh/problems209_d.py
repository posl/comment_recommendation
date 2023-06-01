Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    roads = []
    for i in range(n-1):
        roads.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        if query[0] > query[1]:
            query[0], query[1] = query[1], query[0]
        for road in roads:
            if road[0] > road[1]:
                road[0], road[1] = road[1], road[0]
        if query[0] == query[1]:
            print('Town')
        else:
            for road in roads:
                if query[0] == road[0] and query[1] == road[1]:
                    print('Road')
                    break
                elif query[0] == road[0] and query[1] == road[1]:
                    print('Road')
                    break
                elif query[0] > road[0] and query[1] < road[1]:
                    print('Town')
                    break
                elif query[0] < road[0] and query[1] > road[1]:
                    print('Town')
                    break
            else:
                print('Road')

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    #print(n, q)
    #print(type(n), type(q))
    #print("n = ", n, "q = ", q)
    #print("n = %d, q = %d" % (n, q))
    #print("n = {0}, q = {1}".format(n, q))

    # 读取道路信息
    roads = []
    for i in range(n - 1):
        road = list(map(int, input().split()))
        roads.append(road)
    #print(roads)

    # 读取查询信息
    queries = []
    for i in range(q):
        query = list(map(int, input().split()))
        queries.append(query)
    #print(queries)

    # 构建图
    graph = {}
    for road in roads:
        if road[0] not in graph:
            graph[road[0]] = [road[1]]
        else:
            graph[road[0]].append(road[1])

        if road[1] not in graph:
            graph[road[1]] = [road[0]]
        else:
            graph[road[1]].append(road[0])
    #print(graph)

    # 构建距离表
    distance = {}
    for i in range(1, n + 1):
        distance[i] = -1
    #print(distance)

    # 深度优先搜索
    def dfs(graph, start, distance):
        #print("start = ", start)
        #print("distance = ", distance)
        #print("graph = ", graph)
        for node in graph[start]:
            if distance[node] == -1:
                distance[node] = distance[start] + 1
                dfs(graph, node, distance)

    # 计算所有节点到根节点的距离
    distance[1] = 0
    dfs(graph, 1, distance)
    #print(distance)

    # 处理查询
    for query in queries:
        #print(query)
        #print(distance[query[0]], distance[query[1]])
        if (distance[query[0]] % 2) == (distance[query[1]] % 2):
            print("Town")
        else:

=======
Suggestion 3

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

=======
Suggestion 4

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]

=======
Suggestion 5

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # print(N, Q)
    # print(type(N), type(Q))
    # print(type(N), type(Q))
    # print(type(N), type(Q))

    # a = [0] * (N - 1)
    # b = [0] * (N - 1)
    # c = [0] * Q
    # d = [0] * Q
    # for i in range(N - 1):
    #     a[i], b[i] = map(int, input().split())
    # for i in range(Q):
    #     c[i], d[i] = map(int, input().split())

    # print(a, b, c, d)

    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)

    # print(graph)
    # print(graph[1][0])
    # print(graph[graph[1][0]][0])
    # print(graph[graph[graph[1][0]][0]][0])
    # print(graph[graph[graph[graph[1][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0]][0]][0])
    # print(graph[graph[graph[graph[graph[graph[graph[graph[graph[1][0]][0]][0]][0]][0]][0]][0]][0]][0])

    # print(graph[1][0])
    # print(graph[graph[1][0]][0])
    # print(graph[graph[graph[1][0]][0]][0])
    # print(graph[graph[graph[graph[1][0]][0]][

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    towns = []
    roads = []
    for i in range(N-1):
        a, b = map(int, input().split())
        #print(a, b)
        towns.append([a, b])
    for i in range(Q):
        c, d = map(int, input().split())
        #print(c, d)
        roads.append([c, d])
    for i in range(Q):
        c = roads[i][0]
        d = roads[i][1]
        #print(c, d)
        if c == d:
            print("Town")
            continue
        #print(c, d)
        if c > d:
            c, d = d, c
        #print(c, d)
        for j in range(N-1):
            if towns[j][0] == c and towns[j][1] == d:
                print("Town")
                break
            if towns[j][0] == c and towns[j][1] > d:
                print("Town")
                break
            if towns[j][0] > c and towns[j][1] == d:
                print("Town")
                break
            if towns[j][0] > c and towns[j][1] < d:
                print("Road")
                break
        else:
            print("Road")
    return 0

=======
Suggestion 8

def main():
    return

=======
Suggestion 9

def main():
    pass
