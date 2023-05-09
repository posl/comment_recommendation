def main():
    #Read input
    N, M = map(int, input().split())
    #Roads
    roads = []
    for i in range(M):
        a, b = map(int, input().split())
        roads.append([a, b])
    #Count
    cnt = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            #Check if a road exists
            road_exists = False
            for k in range(M):
                if roads[k][0] == i and roads[k][1] == j:
                    road_exists = True
            if road_exists:
                cnt += 1
    #Output
    print(cnt)
