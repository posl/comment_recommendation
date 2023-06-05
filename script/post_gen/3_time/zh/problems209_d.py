Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    road = []
    town = []
    for i in range(n-1):
        road.append(list(map(int, input().split())))
    for i in range(q):
        town.append(list(map(int, input().split())))
    for i in range(q):
        if town[i][0] == town[i][1]:
            print("Town")
        else:
            for j in range(n-1):
                if road[j][0] == town[i][0] and road[j][1] == town[i][1]:
                    print("Town")
                    break
                elif road[j][0] == town[i][1] and road[j][1] == town[i][0]:
                    print("Town")
                    break
                elif road[j][0] == town[i][0] or road[j][1] == town[i][0]:
                    if road[j][0] == town[i][1] or road[j][1] == town[i][1]:
                        print("Road")
                        break
                elif road[j][0] == town[i][1] or road[j][1] == town[i][1]:
                    if road[j][0] == town[i][0] or road[j][1] == town[i][0]:
                        print("Road")
                        break
                else:
                    print("Road")
                    break
main()

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    road = [[0 for i in range(n)] for j in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        road[a-1][b-1] = 1
        road[b-1][a-1] = 1
    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if road[c][d] == 1:
            print("Road")
        else:
            print("Town")

=======
Suggestion 5

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

=======
Suggestion 6

def findRoot(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = findRoot(parent, parent[x])
        return parent[x]

=======
Suggestion 7

def main():
    n,q = map(int,raw_input().split())
    roads = []
    for i in range(n-1):
        a,b = map(int,raw_input().split())
        roads.append((a,b))
    for i in range(q):
        c,d = map(int,raw_input().split())
        if (c,d) in roads or (d,c) in roads:
            print "Road"
        else:
            print "Town"

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N-1)]
    CD = [list(map(int, input().split())) for i in range(Q)]

    # print(N, Q)
    # print(AB)
    # print(CD)

    # 1. 从AB中找到C和D的位置
    # 2. 如果C和D相邻，输出Road
    # 3. 如果C和D不相邻，输出Town
    # 4. 如果C和D在同一条线上，输出Road
    # 5. 如果C和D不在同一条线上，输出Town
    # 6. 如果C和D在同一条线上，输出Road
    # 7. 如果C和D不在同一条线上，输出Town
    # 8. 如果C和D在同一条线上，输出Road
    # 9. 如果C和D不在同一条线上，输出Town

    # 1. 从AB中找到C和D的位置
    # 2. 如果C和D相邻，输出Road
    # 3. 如果C和D不相邻，输出Town
    # 4. 如果C和D在同一条线上，输出Road
    # 5. 如果C和D不在同一条线上，输出Town
    # 6. 如果C和D在同一条线上，输出Road
    # 7. 如果C和D不在同一条线上，输出Town
    # 8. 如果C和D在同一条线上，输出Road
    # 9. 如果C和D不在同一条线上，输出Town

    # 1. 从AB中找到C和D的位置
    # 2. 如果C和D相邻，输出Road
    # 3. 如果C和D不相邻，输出Town
    # 4. 如果C和D在同一条线上，输出Road
    # 5. 如果C和D不在同一条线上，输出Town
    # 6. 如果

=======
Suggestion 9

def findRoot(root, x):
    if root[x] == x:
        return x
    else:
        root[x] = findRoot(root, root[x])
        return root[x]

=======
Suggestion 10

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
