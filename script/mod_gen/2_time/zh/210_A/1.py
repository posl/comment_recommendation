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

if __name__ == '__main__':
    main()