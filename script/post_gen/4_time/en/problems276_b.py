Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    #print("A: ", A)
    #print("B: ", B)

    #print("N: ", N)
    #print("M: ", M)

    print("N: ", N)
    print("M: ", M)

    print("A: ", A)
    print("B: ", B)

    print("N: ", N)
    print("M: ", M)

    print("A:

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    cities = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        cities[a-1].append(b)
        cities[b-1].append(a)
    for city in cities:
        print(len(city), *sorted(city))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    d = [0] * N
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        d[A] += 1
        d[B] += 1
        a[A].append(B)
        a[B].append(A)
    for i in range(N):
        ans = [d[i]]
        ans.extend(sorted(a[i]))
        print(' '.join(map(str, ans)))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    for i in range(n):
        count = 0
        for j in range(m):
            if road[j][0] == i+1 or road[j][1] == i+1:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    road.sort()
    city = [[] for i in range(n)]
    for i in range(m):
        city[road[i][0]-1].append(road[i][1])
    for i in range(n):
        print(len(city[i]))
        for j in range(len(city[i])):
            print(city[i][j])

=======
Suggestion 6

def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    a = [0] * N
    b = [0] * N
    for i in range(M):
        a[i], b[i] = input().split()
        a[i] = int(a[i])
        b[i] = int(b[i])
    for i in range(N):
        c = 0
        for j in range(M):
            if a[j] == i + 1:
                c += 1
            elif b[j] == i + 1:
                c += 1
        print(c)

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    roads.sort()
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])
    for city in cities:
        print(len(city), *city)

=======
Suggestion 8

def main():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, sys.stdin.readline().split())))
    roads.sort()
    cities = [[] for i in range(n)]
    for i in roads:
        cities[i[0]-1].append(i[1])
    for i in range(n):
        print(len(cities[i]), end=' ')
        for j in cities[i]:
            print(j, end=' ')
        print()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    #print(roads)
    cities = {}
    for road in roads:
        if road[0] not in cities:
            cities[road[0]] = [road[1]]
        else:
            cities[road[0]].append(road[1])
        if road[1] not in cities:
            cities[road[1]] = [road[0]]
        else:
            cities[road[1]].append(road[0])
    #print(cities)
    for i in range(1, n+1):
        if i in cities:
            print(len(cities[i])+1, end=" ")
            print(*sorted(cities[i]))
        else:
            print(0)

=======
Suggestion 10

def get_input():
    n, m = map(int, input().split())
    return n, m
