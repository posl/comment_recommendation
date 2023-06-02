Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # 与城市i直接相连的城市数量（1 ≦ i ≦ N），这些城市为城市a_{i, 1}, ..., 城市a_{i, d_i}，依次递增

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    d = [0] * n
    a = [[] for _ in range(n)]
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        d[ai] += 1
        d[bi] += 1
        a[ai].append(bi)
        a[bi].append(ai)
    for i in range(n):
        print(d[i], end=' ')
        for j in range(d[i]):
            print(a[i][j] + 1, end=' ')
        print()

=======
Suggestion 3

def get_data():
    N, M = input().split()
    N = int(N)
    M = int(M)
    data = []
    for i in range(M):
        a, b = input().split()
        a = int(a)
        b = int(b)
        data.append([a, b])
    return N, M, data

=======
Suggestion 4

def print_road(n, m, road):
    road = sorted(road, key=lambda x: x[0])
    for i in range(n):
        res = [0]
        for j in range(m):
            if road[j][0] == i+1:
                res.append(road[j][1])
        print(len(res)-1, end=' ')
        print(*res[1:])

=======
Suggestion 5

def print_city(road):
    road.sort(key=lambda x: (x[0], x[1]))
    city = [0] * (N + 1)
    for i in range(M):
        city[road[i][0]] += 1
        city[road[i][1]] += 1
    for i in range(1, N + 1):
        print(city[i], end=' ')
        for j in range(M):
            if i == road[j][0]:
                print(road[j][1], end=' ')
            elif i == road[j][1]:
                print(road[j][0], end=' ')
        print()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        a, b = map(int, input().split())
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
        if b not in d:
            d[b] = [a]
        else:
            d[b].append(a)
    for i in range(1, n+1):
        if i in d:
            d[i].sort()
            print(len(d[i]), end=' ')
            for j in d[i]:
                print(j, end=' ')
            print()
        else:
            print(0)

=======
Suggestion 7

def main():
    n,m=map(int,input().split())
    a,b=[],[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(1,n+1):
        count=0
        for j in range(m):
            if i==a[j] or i==b[j]:
                count+=1
        print(count,end=" ")
        for j in range(m):
            if i==a[j] or i==b[j]:
                if i==a[j]:
                    print(b[j],end=" ")
                else:
                    print(a[j],end=" ")
        print()

main()

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    #print(n, m)
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    #print(roads)
    cities = []
    for i in range(n):
        cities.append([])
    for road in roads:
        cities[road[0] - 1].append(road[1])
        cities[road[1] - 1].append(road[0])
    #print(cities)
    for city in cities:
        city.sort()
    #print(cities)
    for city in cities:
        print(len(city), end=' ')
        for c in city:
            print(c, end=' ')
        print()

=======
Suggestion 9

def getCityCount(cityCount, citys):
    for i in range(1, cityCount + 1):
        count = 0
        citys = sorted(citys, key=lambda x: x[0])
        for j in range(len(citys)):
            if i in citys[j]:
                count += 1
                citys[j].remove(i)
        print(count, end=' ')
        for j in range(count):
            print(citys[j][0], end=' ')
        print()

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    ab = []
    for i in range(M):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    #print(ab)
    res = [[] for i in range(N)]
    for i in range(M):
        res[ab[i][0]-1].append(ab[i][1])
        res[ab[i][1]-1].append(ab[i][0])
    #print(res)
    for i in range(N):
        res[i].sort()
        print(len(res[i]), end=' ')
        print(*res[i])
