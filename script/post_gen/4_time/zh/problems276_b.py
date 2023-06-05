Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    #print(n, m)
    #

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    data = []
    for i in range(M):
        data.append(list(map(int, input().split())))
    data.sort()
    for i in range(N):
        count = 0
        for j in range(M):
            if i+1 in data[j]:
                count += 1
        print(count, end=' ')
        for j in range(M):
            if i+1 in data[j]:
                print(data[j][0] if data[j][0] != i+1 else data[j][1], end=' ')
        print()

=======
Suggestion 3

def getCityInfo(N, M, citys):
    cityInfo = [0] * N
    for i in range(M):
        cityInfo[citys[i][0] - 1] += 1
        cityInfo[citys[i][1] - 1] += 1
    return cityInfo

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    #print(AB)
    #print(N, M)
    #print(AB)
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])
    #print(AB[9][0])
    #print(AB[9][1])
    #print(AB[10][0])
    #print(AB[10][1])
    #print(AB[11][0])
    #print(AB[11][1])
    #print(AB[12][0])
    #print(AB[12][1])
    #print(AB[13][0])
    #print(AB[13][1])
    #print(AB[14][0])
    #print(AB[14][1])
    #print(AB[15][0])
    #print(AB[15][1])
    #print(AB[16][0])
    #print(AB[16][1])
    #print(AB[17][0])
    #print(AB[17][1])
    #print(AB[18][0])
    #print(AB[18][1])
    #print(AB[19][0])
    #print(AB[19][1])
    #print(AB[20][0])
    #print(AB[20][1])
    #print(AB[21][0])
    #print(AB[21][1])
    #print(AB

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))

    city = [[] for i in range(n)]
    for i in range(m):
        city[road[i][0]-1].append(road[i][1])
        city[road[i][1]-1].append(road[i][0])

    for i in range(n):
        print(len(city[i]), end = ' ')
        for j in range(len(city[i])):
            print(city[i][j], end = ' ')
        print()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        print(len(graph[i]), end=" ")
        for j in sorted(graph[i]):
            print(j+1, end=" ")
        print()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    city = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        city[a-1].append(b)
        city[b-1].append(a)
    for i in range(n):
        city[i].sort()
        print(len(city[i]), end=' ')
        for j in range(len(city[i])):
            print(city[i][j], end=' ')
        print()

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    node = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        node[a-1].append(b)
        node[b-1].append(a)
    for i in range(n):
        print(len(node[i]),end=' ')
        for j in node[i]:
            print(j,end=' ')
        print()

=======
Suggestion 9

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    # 建立邻接表
    adj = [[] for _ in range(n)]
    for i in range(m):
        adj[a[i] - 1].append(b[i] - 1)
        adj[b[i] - 1].append(a[i] - 1)
    # 打印结果
    for i in range(n):
        print(len(adj[i]), end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j] + 1, end=" ")
        print()

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    d = [0 for i in range(n)]
    a = [[] for i in range(n)]
    for i in range(m):
        a1,a2 = map(int,input().split())
        a1 -= 1
        a2 -= 1
        a[a1].append(a2)
        a[a2].append(a1)
        d[a1] += 1
        d[a2] += 1
    for i in range(n):
        print(d[i],end=' ')
        for j in range(d[i]):
            print(a[i][j]+1,end=' ')
        print()
