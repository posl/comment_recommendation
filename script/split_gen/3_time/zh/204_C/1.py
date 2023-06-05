def main():
    n,m = map(int,input().split())
    road = []
    for _ in range(m):
        road.append(list(map(int,input().split())))
    #print(road)
    road = sorted(road,key = lambda x:x[0])
    #print(road)
    start = []
    end = []
    for i in range(m):
        start.append(road[i][0])
        end.append(road[i][1])
    #print(start,end)
    #print(road)
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][0] == road[j][1]:
                start.append(road[j][0])
                end.append(road[i][1])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][1] == road[j][0]:
                start.append(road[i][0])
                end.append(road[j][1])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][1] == road[j][1]:
                start.append(road[i][0])
                end.append(road[j][0])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][0] == road[j][0]:
                start.append(road[j][1])
                end.append(road[i][1])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][0] == road[j][0]:
                start.append(road[i][1])
                end.append(road[j][1])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][1] == road[j][1]:
                start.append(road[j][0])
                end.append(road[i][0])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][1] == road[j][0]:
                start.append(road[i][0])
                end.append(road[j][1])
    #print(start,end)
    for i in range(m):
        for j in range(m):
            if road[i][0] == road[j][1]:
                start.append(road[j
