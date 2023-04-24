Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    for i in range(N):
        G[i].sort()
        print(len(G[i]), *map(lambda x: x+1, G[i]))

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    for i in range(N):
        road[i].sort()
        print(len(road[i]), *road[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    a = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        a[A - 1].append(B)
        a[B - 1].append(A)
    for i in range(N):
        a[i] = sorted(a[i])
        print(len(a[i]), end = ' ')
        for j in range(len(a[i])):
            print(a[i][j], end = ' ')
        print('')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    path = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        path[a-1].add(b-1)
        path[b-1].add(a-1)
    for i in range(N):
        print(len(path[i]), *sorted(path[i])+1)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append((a, b))
    roads.sort()
    prev = 1
    cnt = 0
    ans = []
    for a, b in roads:
        if a != prev:
            ans.append([cnt] + [i for i in range(prev, a)])
            prev = a
            cnt = 0
        cnt += 1
    ans.append([cnt] + [i for i in range(prev, n + 1)])
    for a in ans:
        print(' '.join(map(str, a)))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(N):
        cities.append([i+1])
    for i in range(M):
        A, B = map(int, input().split())
        cities[A-1].append(B)
        cities[B-1].append(A)
    for i in range(N):
        cities[i].sort()
        print(len(cities[i])-1, end=" ")
        for j in range(len(cities[i])-1):
            print(cities[i][j+1], end=" ")
        print()

=======
Suggestion 7

def main():
    #input
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    #compute
    A = [[] for _ in range(N)]
    for a, b in AB:
        A[a-1].append(b)
        A[b-1].append(a)
    for i in range(N):
        A[i].sort()
        A[i] = [len(A[i])] + A[i]

    #output
    for a in A:
        print(*a)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort()
    connections = [[] for _ in range(N)]
    for road in roads:
        connections[road[0]-1].append(road[1])
        connections[road[1]-1].append(road[0])
    for i in range(N):
        print(len(connections[i]), end=' ')
        for j in range(len(connections[i])):
            print(connections[i][j], end=' ')
        print()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 連結リスト
    connect = {i:[] for i in range(1, N+1)}
    for i in range(M):
        A, B = map(int, input().split())
        connect[A].append(B)
        connect[B].append(A)
    for i in range(1, N+1):
        connect[i].sort()
        print(len(connect[i]), *connect[i])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #print(N,M)
    #print("

")
    road = []
    for i in range(M):
        road.append(list(map(int, input().split())))
    #print(road)
    #print("

")
    d = {}
    for i in range(1,N+1):
        #print(i)
        d[i] = []
        for j in range(M):
            #print(j)
            if i in road[j]:
                if i == road[j][0]:
                    d[i].append(road[j][1])
                else:
                    d[i].append(road[j][0])
        d[i].sort()
        print(len(d[i]),end = " ")
        for k in d[i]:
            print(k,end = " ")
        print("

")
