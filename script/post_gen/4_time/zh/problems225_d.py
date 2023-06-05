Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]

=======
Suggestion 2

def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

=======
Suggestion 3

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    cars = [[] for _ in range(N+1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            cars[query[2]].extend(cars[query[1]])
            cars[query[1]] = []
        elif query[0] == 2:
            cars[query[1]].extend(cars[query[2]])
            cars[query[2]] = []
        else:
            print(' '.join(map(str, cars[query[1]])))

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    l = [i for i in range(n+1)]
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            l[query[1]],l[query[2]] = l[query[2]],l[query[1]]
        elif query[0] == 2:
            l[query[1]],l[query[2]] = l[query[2]],l[query[1]]
        else:
            ans = []
            for i in range(n+1):
                if l[i] == l[query[1]]:
                    ans.append(i)
            print(len(ans),*ans)

=======
Suggestion 6

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 7

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 8

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
