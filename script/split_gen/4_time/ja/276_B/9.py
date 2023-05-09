def main():
    n, m = map(int, input().split())
    road = [list(map(int, input().split())) for i in range(m)]
    road.sort()
    #print(road)
    city = [0]*n
    #print(city)
    for i in range(m):
        city[road[i][0]-1] += 1
        city[road[i][1]-1] += 1
    #print(city)
    for i in range(n):
        print(city[i])
