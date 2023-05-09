Synthesizing 10/10 solutions

=======
Suggestion 1

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 2

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    train = [[] for _ in range(N)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1].append(query[2]-1)
        elif query[0] == 2:
            train[query[1]-1].remove(query[2]-1)
        else:
            print(*train[query[1]-1])

=======
Suggestion 5

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 6

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    cars = [i for i in range(n)]
    front = [i for i in range(n)]
    back = [i for i in range(n)]
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            front[back[cars[query[2]-1]]] = front[cars[query[1]-1]]
            back[front[cars[query[1]-1]]] = back[cars[query[2]-1]]
            front[cars[query[1]-1]] = cars[query[2]-1]
            back[cars[query[2]-1]] = cars[query[1]-1]
            cars[query[2]-1] = cars[query[1]-1]
        elif query[0] == 2:
            front[back[cars[query[2]-1]]] = cars[query[1]-1]
            back[front[cars[query[1]-1]]] = cars[query[2]-1]
            cars[query[1]-1] = front[cars[query[1]-1]]
            cars[query[2]-1] = back[cars[query[2]-1]]
            front[cars[query[1]-1]] = query[1]-1
            back[cars[query[2]-1]] = query[2]-1
        else:
            ans = []
            car = cars[query[1]-1]
            while car != n:
                ans.append(car+1)
                car = front[car]
            print(len(ans), *ans)
    return

=======
Suggestion 8

def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

=======
Suggestion 9

def get_representative(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = get_representative(parents[x])
        return parents[x]

=======
Suggestion 10

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
