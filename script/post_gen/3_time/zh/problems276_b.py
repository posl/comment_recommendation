Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort(key=lambda x:x[1])
    roads.sort(key=lambda x:x[0])
    ans = [[] for i in range(n)]
    for i in range(m):
        ans[roads[i][0]-1].append(roads[i][1])
        ans[roads[i][1]-1].append(roads[i][0])
    for i in range(n):
        ans[i].insert(0, len(ans[i]))
        print(" ".join(map(str, ans[i])))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    roads.sort(key=lambda x: x[1])
    roads.sort(key=lambda x: x[0])
    roads = [[roads[0][0], roads[0][1], 1]]
    for i in range(1, m):
        if roads[-1][0] == roads[i][0]:
            if roads[-1][1] == roads[i][1] - 1:
                roads[-1][2] += 1
            else:
                roads.append([roads[i][0], roads[i][1], 1])
        else:
            roads.append([roads[i][0], roads[i][1], 1])
    i, j = 0, 0
    while i < n:
        if j < len(roads) and roads[j][0] == i + 1:
            print(roads[j][2], *range(roads[j][1] - roads[j][2] + 1, roads[j][1] + 1))
            j += 1
        else:
            print(0)
        i += 1

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))

    # print(roads)
    # print(n, m)
    # n, m = 5, 10
    # roads = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [
    #     2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    # roads = [[3, 6], [1, 3], [5, 6], [2, 5], [1, 2], [1, 6]]
    # print(roads)

    # print(n, m)
    # print(roads)

    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])

    for city in cities:
        city.sort()

    for city in cities:
        print(len(city), end=' ')
        for c in city:
            print(c, end=' ')
        print()

=======
Suggestion 4

def main():
    n,m=map(int,input().split())
    a,b=[],[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(1,n+1):
        print(a.count(i)+b.count(i))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    cities = [set() for _ in range(n)]
    for road in roads:
        cities[road[0]-1].add(road[1])
        cities[road[1]-1].add(road[0])
    for city in cities:
        print(len(city), end=' ')
        print(*sorted(city))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    edge = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        edge[A-1].append(B)
        edge[B-1].append(A)
    for i in range(N):
        edge[i].sort()
    for i in range(N):
        print(len(edge[i]), end=' ')
        for j in range(len(edge[i])):
            print(edge[i][j], end=' ')
        print()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    city = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        city[a-1].append(b)
        city[b-1].append(a)
    for i in range(n):
        print(len(city[i]), *sorted(city[i]))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print(type(N), type(M))
    road = []
    for i in range(M):
        road.append(list(map(int, input().split())))
    #print(road)
    #print(type(road))
    #print(road[0][0])
    #print(road[0][1])
    #print(road[1][0])
    #print(road[1][1])
    #print(road[2][0])
    #print(road[2][1])
    #print(road[3][0])
    #print(road[3][1])
    #print(road[4][0])
    #print(road[4][1])
    #print(road[5][0])
    #print(road[5][1])
    #print(road[6][0])
    #print(road[6][1])
    #print(road[7][0])
    #print(road[7][1])
    #print(road[8][0])
    #print(road[8][1])
    #print(road[9][0])
    #print(road[9][1])
    #print(road[10][0])
    #print(road[10][1])
    #print(road[11][0])
    #print(road[11][1])
    #print(road[12][0])
    #print(road[12][1])
    #print(road[13][0])
    #print(road[13][1])
    #print(road[14][0])
    #print(road[14][1])
    #print(road[15][0])
    #print(road[15][1])
    #print(road[16][0])
    #print(road[16][1])
    #print(road[17][0])
    #print(road[17][1])
    #print(road[18][0])
    #print(road[18][1])
    #print(road[19][0])
    #print(road[19][1])
    #print(road[20][0])
    #print(road[20][1])
    #print(road[21][0])
    #print(road

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 一个dict，key是城市编号，value是与之相连的城市编号的list
    cities = {}
    # 读取M条道路
    for i in range(M):
        A, B = map(int, input().split())
        if A not in cities:
            cities[A] = [B]
        else:
            cities[A].append(B)
        if B not in cities:
            cities[B] = [A]
        else:
            cities[B].append(A)
    # 按照题目要求，打印N行
    for i in range(1, N + 1):
        if i in cities:
            print(len(cities[i]), *sorted(cities[i]))
        else:
            print(0)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    cities = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        cities[a-1].append(b)
        cities[b-1].append(a)

    for i in range(n):
        print(len(cities[i]), *sorted(cities[i]))
