Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])
    for city in cities:
        print(len(city), *sorted(city))

=======
Suggestion 2

def get_input():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    return N, M, A, B

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for i in range(M)]

    cities = [[] for i in range(N)]
    for i in range(M):
        cities[roads[i][0] - 1].append(roads[i][1])
        cities[roads[i][1] - 1].append(roads[i][0])

    for i in range(N):
        cities[i].sort()
        cities[i].insert(0, len(cities[i]))
        print(' '.join(map(str, cities[i])))

=======
Suggestion 4

def problem276_b():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append([a, b])
    roads.sort()
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0] - 1].append(road[1])
    for city in cities:
        print(len(city), *city)

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    l = []
    for i in range(m):
        a,b = map(int, input().split())
        l.append(a)
        l.append(b)

    for i in range(1,n+1):
        print(l.count(i))

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0] - 1].append(road[1])
        cities[road[1] - 1].append(road[0])
    for city in cities:
        print(len(city), *sorted(city))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))
    roads.sort()
    cities = [0] * N
    for i in range(M):
        cities[roads[i][0] - 1] += 1
        cities[roads[i][1] - 1] += 1
    for i in range(N):
        print(cities[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))
    cities = [[0] for _ in range(N)]
    for i in range(M):
        cities[roads[i][0]-1].append(roads[i][1])
        cities[roads[i][1]-1].append(roads[i][0])
    for i in range(N):
        cities[i].sort()
    for i in range(N):
        print(len(cities[i])-1, end=" ")
        for j in range(1, len(cities[i])):
            print(cities[i][j], end=" ")
        print()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort()
    for i in range(n):
        count = 0
        for j in range(m):
            if roads[j][0] == i + 1:
                count += 1
        print(count, end = " ")
        for j in range(m):
            if roads[j][0] == i + 1:
                print(roads[j][1], end = " ")
        print("")

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    roads = []
    for i in range(m):
        a,b = map(int,input().split())
        roads.append([a,b])

    cities = []
    for i in range(n):
        cities.append([])

    for i in range(m):
        cities[roads[i][0]-1].append(roads[i][1])
        cities[roads[i][1]-1].append(roads[i][0])

    for i in range(n):
        cities[i].sort()
        print(len(cities[i]))
        print(*cities[i])
