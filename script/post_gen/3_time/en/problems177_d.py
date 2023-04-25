Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1)
    print(uf.groups)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    groups = [0] * N
    group = 1
    for i in range(N):
        if groups[i] == 0:
            groups[i] = group
            q = [i]
            while q:
                p = q.pop()
                for f in friends[p]:
                    if groups[f] == 0:
                        groups[f] = group
                        q.append(f)
            group += 1
    print(group - 1)

main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    friends = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)

    for i in range(N):
        if friends[i]:
            for j in friends[i]:
                friends[i] |= friends[j]

    print(len({frozenset(f) for f in friends}))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        if E[i] == []:
            ans += 1
            continue
        v = [False] * N
        v[i] = True
        q = [i]
        while q:
            w = q.pop()
            for e in E[w]:
                if not v[e]:
                    v[e] = True
                    q.append(e)
        if not all(v):
            ans += 1
    print(ans)

=======
Suggestion 5

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    friends = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #print(friends)
    group = [-1]*n
    num_group = 0
    for i in range(n):
        if group[i] == -1:
            group[i] = num_group
            num_group += 1
        for j in friends[i]:
            if group[j] == -1:
                group[j] = group[i]
    print(num_group)

=======
Suggestion 7

def main():
  n,m = map(int,input().split())
  g = [[] for i in range(n)]
  for i in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
  ans = 0
  for i in range(n):
    ans = max(ans, len(g[i])+1)
  print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [[a-1, b-1] for a, b in AB]
    AB = [[a, b] if a < b else [b, a] for a, b in AB]
    AB = list(set([tuple(a) for a in AB]))
    AB = sorted(AB, key=lambda x: x[0])
    AB = sorted(AB, key=lambda x: x[1])
    d = {}
    for a, b in AB:
        if a not in d:
            d[a] = []
        d[a].append(b)
    ans = 0
    while len(d) > 0:
        ans += 1
        k = list(d.keys())[0]
        q = [k]
        while len(q) > 0:
            k = q.pop()
            if k in d:
                for v in d[k]:
                    q.append(v)
                del d[k]
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    AB = sorted(AB)
    AB = sorted(AB, key=lambda x:x[0])
    AB = sorted(AB, key=lambda x:x[1])
    
    ans = 1
    if N == 2:
        ans = 1
    else:
        ans = 2
        for i in range(1, len(AB)):
            if AB[i][0] == AB[i-1][0] and AB[i][1] == AB[i-1][1]:
                continue
            else:
                ans += 1
    print(ans)

=======
Suggestion 10

def read_int():
    return int(input())
