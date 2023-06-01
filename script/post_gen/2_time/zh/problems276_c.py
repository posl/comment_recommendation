Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for i in range(m)]
    cities = [[] for i in range(n)]
    for a, b in roads:
        cities[a-1].append(b)
        cities[b-1].append(a)
    for i in range(n):
        print(len(cities[i]), end=" ")
        print(*sorted(cities[i]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    # print(N, M, AB)

    # 1. 与城市i直接相连的城市数量（1 ≦ i ≦ N）
    # 2. 这些城市为城市a_{i, 1}, ..., 城市a_{i, d_i}，依次递增。
    # 3. 第i行（1 ≦ i ≦ N）应该包含d_i + 1个整数d_i, a_{i, 1}, ..., a_{i, d_i}，按照这个顺序，用空格分开。

    # 1. 与城市i直接相连的城市数量（1 ≦ i ≦ N）
    # N = 6
    # M = 6
    # AB = [[3, 6], [1, 3], [5, 6], [2, 5], [1, 2], [1, 6]]

    # 1. 与城市i直接相连的城市数量（1 ≦ i ≦ N）
    # 2. 这些城市为城市a_{i, 1}, ..., 城市a_{i, d_i}，依次递增。
    # 3. 第i行（1 ≦ i ≦ N）应该包含d_i + 1个整数d_i, a_{i, 1}, ..., a_{i, d_i}，按照这个顺序，用空格分开。

    # 1. 与城市i直接相连的城市数量（1 ≦ i ≦ N）
    # 2. 这些城市为城市a_{i, 1}, ..., 城市a_{i, d_i}，依次递增。
    # 3. 第i行（1 ≦ i ≦ N）应该包含d_i + 1个整数d_i, a_{i, 1}, ..., a_{i, d_i}，按照

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort(key=lambda x: x[1])
    roads.sort(key=lambda x: x[0])
    for i in range(1, n+1):
        print(len([x for x in roads if x[0] == i]) + len([x for x in roads if x[1] == i]), end=' ')
        for x in roads:
            if x[0] == i:
                print(x[1], end=' ')
            elif x[1] == i:
                print(x[0], end=' ')
        print()

=======
Suggestion 5

def problem276_b():
    return None

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    a.sort()
    b = []
    for i in range(n):
        b.append([])
    for i in range(m):
        b[a[i][0]-1].append(a[i][1])
        b[a[i][1]-1].append(a[i][0])
    for i in range(n):
        b[i].sort()
    for i in range(n):
        print(len(b[i]), end = " ")
        for j in range(len(b[i])):
            print(b[i][j], end = " ")
        print()

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    road = []
    for i in range(m):
        road.append(list(map(int,input().split())))
    road.sort()
    for i in range(1,n+1):
        print(len([j for j in road if j[0] == i or j[1] == i]),end = ' ')
        for j in road:
            if j[0] == i and j[1] != i:
                print(j[1],end = ' ')
            elif j[1] == i and j[0] != i:
                print(j[0],end = ' ')
        print()
main()

=======
Suggestion 8

def main():
    # 读入数据
    n, m = map(int, input().split())
    # 城市编号从0开始
    roads = [[int(i)-1 for i in input().split()] for _ in range(m)]
    # 初始化城市
    cities = [[] for _ in range(n)]
    # 为每个城市添加相连的城市
    for road in roads:
        # 两个方向都要添加
        cities[road[0]].append(road[1])
        cities[road[1]].append(road[0])
    # 打印输出
    for city in cities:
        print(len(city), *sorted(city))

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = [0]*n
    b = [0]*n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(n):
        count = 0
        for j in range(m):
            if a[j] == i+1:
                count += 1
            elif b[j] == i+1:
                count += 1
        print(count,end=' ')
        for j in range(m):
            if a[j] == i+1:
                print(b[j],end=' ')
            elif b[j] == i+1:
                print(a[j],end=' ')
        print()
