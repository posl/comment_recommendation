Synthesizing 10/10 solutions

=======
Suggestion 1

def get_city_num(n, m, road_list):
    city_num_list = [0 for i in range(n)]
    for road in road_list:
        city_num_list[road[0] - 1] += 1
        city_num_list[road[1] - 1] += 1

    return city_num_list

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        x, y = map(int, input().split())
        a[x - 1] += 1
        a[y - 1] += 1
    for i in range(n):
        print(a[i])

=======
Suggestion 3

def main():
    [N, M] = [int(x) for x in input().split()]
    roads = [[int(x) for x in input().split()] for i in range(M)]
    #print(roads)
    cities = [[] for i in range(N)]
    for i in range(M):
        cities[roads[i][0]-1].append(roads[i][1])
        cities[roads[i][1]-1].append(roads[i][0])
    #print(cities)
    #cities = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    for i in range(N):
        cities[i].sort()
        cities[i].insert(0,len(cities[i]))
        print(*cities[i])
    return 0

=======
Suggestion 4

def main():
    N = 6
    M = 6
    A = [3, 1, 5, 2, 1, 1]
    B = [6, 3, 6, 5, 2, 6]
    # N, M = map(int, input().split())
    # A = [0] * M
    # B = [0] * M
    # for i in range(M):
    #     A[i], B[i] = map(int, input().split())

    # print(N, M)
    # print(A)
    # print(B)

    # 与城市i直接相连的城市数量
    d = [0] * N
    for i in range(M):
        d[A[i] - 1] += 1
        d[B[i] - 1] += 1
    print(d)

    # 与城市i直接相连的城市
    a = [[] for _ in range(N)]
    for i in range(M):
        a[A[i] - 1].append(B[i])
        a[B[i] - 1].append(A[i])
    print(a)

    for i in range(N):
        print(d[i], end=' ')
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    roads = []
    for i in range(m):
        a,b = map(int, input().split())
        roads.append((a,b))
    roads.sort()
    for i in range(1,n+1):
        print(len([road[1] for road in roads if road[0] == i]), end=' ')
        for road in roads:
            if road[0] == i:
                print(road[1], end=' ')
        print()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(1, N + 1):
        print(len([j for j in range(M) if A[j] == i or B[j] == i]))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    cities = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        cities[A-1].append(B)
        cities[B-1].append(A)
    for i in range(N):
        cities[i].sort()
    for i in range(N):
        print(len(cities[i]), end=" ")
        for j in range(len(cities[i])):
            print(cities[i][j], end=" ")
        print()

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    city = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        city[a-1] += 1
        city[b-1] += 1
    for i in range(n):
        print(city[i])

=======
Suggestion 10

def problem276_b():
    pass
