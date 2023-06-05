def main():
    n = int(input())
    roads = []
    for i in range(n-1):
        road = list(map(int, input().split()))
        roads.append(road)
    #print(roads)
    # 路的邻接表
    adjs = [[] for i in range(n+1)]
    for road in roads:
        adjs[road[0]].append(road[1])
        adjs[road[1]].append(road[0])
    #print(adjs)
    # 路的深度
    depths = [0 for i in range(n+1)]
    #print(depths)
    # 路的父亲
    fathers = [0 for i in range(n+1)]
    #print(fathers)
    # 路的访问时间
    visitedTime = [0 for i in range(n+1)]
    #print(visitedTime)
    # 路的离开时间
    leaveTime = [0 for i in range(n+1)]
    #print(leaveTime)
    # 路的访问标志
    visited = [False for i in range(n+1)]
    #print(visited)
    # 路的访问时间
    time = 0
    #print(time)
    # 路的访问序列
    route = []
    #print(route)
    # 路的深度优先遍历
    def dfs(road, depth):
        #print(road, depth)
        # 路的访问时间
        nonlocal time
        time += 1
        visitedTime[road] = time
        #print(visitedTime)
        # 路的访问标志
        visited[road] = True
        #print(visited)
        # 路的深度
        depths[road] = depth
        #print(depths)
        # 路的访问序列
        route.append(road)
        #print(route)
        # 路的访问邻接路
        for adj in adjs[road]:
            if not visited[adj]:
                fathers[adj] = road
                #print(fathers)
                dfs(adj, depth+1)
