Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        ans = 0
        for j in range(M):
            if A[j] == i+1:
                ans += 1
            elif B[j] == i+1:
                ans += 1
        print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    cities = {i: [] for i in range(1, N + 1)}
    for road in roads:
        cities[road[0]].append(road[1])
        cities[road[1]].append(road[0])
    for i in range(1, N + 1):
        print(len(cities[i]), *sorted(cities[i]))

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))

    cities = []
    for i in range(n):
        cities.append([])

    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])

    for city in cities:
        city.sort()

    for city in cities:
        print(len(city), end=" ")
        for c in city:
            print(c, end=" ")
        print()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort()
    cities = []
    for i in range(n):
        cities.append([])
    for i in range(m):
        cities[roads[i][0] - 1].append(roads[i][1])
    for i in range(n):
        print(len(cities[i]), end = ' ')
        for j in range(len(cities[i])):
            print(cities[i][j], end = ' ')
        print()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort()
    for i in range(n):
        cnt = 0
        for j in range(m):
            if roads[j][0] == i+1:
                cnt += 1
            elif roads[j][1] == i+1:
                cnt += 1
        print(cnt)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))
    roads.sort()
    cities = [0 for _ in range(n)]
    for a, b in roads:
        cities[a-1] += 1
        cities[b-1] += 1
    for i in range(n):
        print(cities[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]
    ABs.sort()
    d = {}
    for AB in ABs:
        A = AB[0]
        B = AB[1]
        if A not in d:
            d[A] = [B]
        else:
            d[A].append(B)
        if B not in d:
            d[B] = [A]
        else:
            d[B].append(A)
    for i in range(1, N+1):
        if i not in d:
            print(0)
        else:
            print(len(d[i])+1, end=" ")
            for j in sorted(d[i]):
                print(j, end=" ")
            print()

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int,input().split())))
    roads.sort(key=lambda x: x[0])
    city = [0] * n
    for i in range(m):
        city[roads[i][0]-1] += 1
    for i in range(m):
        city[roads[i][1]-1] += 1
    for i in range(n):
        print(city[i])

=======
Suggestion 9

def get_numbers():
    N,M = map(int, input().split())
    numbers = []
    for i in range(M):
        numbers.append(list(map(int, input().split())))
    return N, M, numbers

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
