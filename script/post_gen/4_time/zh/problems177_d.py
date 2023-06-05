Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))

    # print(N, M)
    # print(AB)

    # 1.所有人都是朋友的情况
    # 2.所有人都不是朋友的情况
    # 3.其他情况
    # 1.所有人都是朋友的情况

    if M == 0:
        print(N)

=======
Suggestion 2

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a - 1].append(b - 1)
        friends[b - 1].append(a - 1)

    colors = [-1] * N
    colors[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in friends[v]:
            if colors[u] == -1:
                colors[u] = 1 - colors[v]
                stack.append(u)
            elif colors[u] == colors[v]:
                print(-1)
                return

    print(colors.count(0), colors.count(1))

=======
Suggestion 4

def findRoot(root, i):
    if root[i] == i:
        return i
    else:
        root[i] = findRoot(root, root[i])
        return root[i]

=======
Suggestion 5

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

=======
Suggestion 6

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    friends = {}
    for i in range(m):
        a,b = map(int,input().split())
        if a in friends:
            friends[a].append(b)
        else:
            friends[a] = [b]
        if b in friends:
            friends[b].append(a)
        else:
            friends[b] = [a]
    #print(friends)
    people = set(range(1,n+1))
    #print(people)
    groups = []
    while people:
        group = set()
        queue = [people.pop()]
        while queue:
            p = queue.pop(0)
            group.add(p)
            if p in friends:
                for f in friends[p]:
                    if f in people:
                        queue.append(f)
                        people.remove(f)
        groups.append(group)
    print(len(groups)-1)

=======
Suggestion 8

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]
