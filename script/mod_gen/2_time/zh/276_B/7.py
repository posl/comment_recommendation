def main():
    n,m = map(int,input().split())
    road = []
    for i in range(m):
        road.append(list(map(int,input().split())))
    for i in range(1,n+1):
        road_i = []
        for j in range(m):
            if road[j][0] == i:
                road_i.append(road[j][1])
            if road[j][1] == i:
                road_i.append(road[j][0])
        road_i.sort()
        print(len(road_i),end=" ")
        for j in range(len(road_i)):
            if j == len(road_i)-1:
                print(road_i[j])
            else:
                print(road_i[j],end=" ")

if __name__ == '__main__':
    main()