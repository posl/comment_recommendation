Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    d = [0] * N
    for i in range(M):
        d[A[i] - 1] += 1
        d[B[i] - 1] += 1
    #print(d)
    a = [[0] * 0 for i in range(N)]
    for i in range(M):
        a[A[i] - 1].append(B[i])
        a[B[i] - 1].append(A[i])
    #print(a)
    for i in range(N):
        a[i].sort()
        print(d[i], end = " ")
        for j in range(d[i]):
            print(a[i][j], end = " ")
        print()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    for i in range(N):
        print(len(G[i]), *sorted(G[i]) + 1)

=======
Suggestion 3

def main():
    from collections import defaultdict
    N, M = map(int, input().split())
    d = defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    for i in range(1, N+1):
        print(len(d[i]), *sorted(d[i]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    city = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        city[A].append(B)
        city[B].append(A)
    for i in range(1, N + 1):
        city[i].sort()
        print(len(city[i]), *city[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    connected_cities = [[] for _ in range(N)]
    for road in roads:
        connected_cities[road[0] - 1].append(road[1])
        connected_cities[road[1] - 1].append(road[0])
    for i in range(N):
        connected_cities[i].sort()
        print(len(connected_cities[i]), *connected_cities[i])
    return

=======
Suggestion 6

def main():
    #input
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    
    #output
    for i in range(1, N+1):
        d = 0
        for j in range(M):
            if i in AB[j]:
                d += 1
        print(d, *sorted([a for a, b in AB if i == a] + [b for a, b in AB if i == b]))

=======
Suggestion 7

def main():
    #input
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]

    #compute
    ans = [[] for _ in range(N)]
    for i in range(M):
        ans[AB[i][0]-1].append(AB[i][1])
        ans[AB[i][1]-1].append(AB[i][0])
    for i in range(N):
        ans[i].sort()
        print(len(ans[i]), *ans[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort()
    ans = [0 for _ in range(N)]
    for i in range(M):
        ans[roads[i][0]-1] += 1
        ans[roads[i][1]-1] += 1
    for i in range(N):
        print(ans[i], end=' ')
        for j in range(M):
            if roads[j][0] == i+1:
                print(roads[j][1], end=' ')
            elif roads[j][1] == i+1:
                print(roads[j][0], end=' ')
        print()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)

=======
Suggestion 10

def main():
    # get input
    n, m = map(int, input().split())
    # create a list of lists
    # the i-th list contains the cities directly connected to city i
    road = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    # sort the lists in ascending order
    for i in range(n):
        road[i].sort()
    # print the results
    for i in range(n):
        print(len(road[i]), end=' ')
        for j in range(len(road[i])):
            print(road[i][j]+1, end=' ')
        print()
