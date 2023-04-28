Synthesizing 10/10 solutions (Duplicates hidden)

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

def main():
    N, Q = map(int, input().split())
    train = [i for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1], train[query[2]-1] = train[query[2]-1], train[query[1]-1]
        elif query[0] == 2:
            train[query[1]-1], train[query[2]-1] = train[query[2]-1], train[query[1]-1]
        else:
            target = train[query[1]-1]
            for i in range(N):
                if target == train[i]:
                    print(i+1, end=' ')
            print()

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    trains = [[i] for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1] - 1, query[2] - 1
            trains[x] += trains[y]
            trains[y] = []
        elif query[0] == 2:
            x, y = query[1] - 1, query[2] - 1
            trains[x] = [trains[x][0]] + trains[x][1:]
            trains[y] = trains[y] + [trains[y][0]]
        elif query[0] == 3:
            x = query[1] - 1
            print(*trains[x])

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    trains = [i for i in range(n)]
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x,y = query[1],query[2]
            if x == y:
                continue
            if trains[x-1] == trains[y-1]:
                continue
            else:
                trains = [trains[x-1] if i == trains[y-1] else i for i in trains]
        elif query[0] == 2:
            x,y = query[1],query[2]
            if x == y:
                continue
            if trains[x-1] != trains[y-1]:
                continue
            else:
                trains = [i if i != trains[x-1] else i+1 for i in trains]
        elif query[0] == 3:
            x = query[1]
            ans = [i+1 for i in range(n) if trains[i] == trains[x-1]]
            print(len(ans),*ans)

=======
Suggestion 6

def getRoot(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getRoot(parent[x])
        return parent[x]

=======
Suggestion 7

def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    train = [ i for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]] = train[query[2]]
        elif query[0] == 2:
            train[query[1]] = query[1]
            train[query[2]] = query[2]
        else:
            print(' '.join(map(str, [i for i, x in enumerate(train) if x == train[query[1]]])))

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    train = [i for i in range(N)]
    for q in query:
        if q[0] == 1:
            train[q[2]-1], train[q[1]-1] = train[q[1]-1], train[q[2]-1]
        elif q[0] == 2:
            train[q[1]-1], train[q[2]-1] = train[q[2]-1], train[q[1]-1]
        else:
            tmp = []
            for i in range(N):
                if train[i] == train[q[1]-1]:
                    tmp.append(i+1)
            ans.append(tmp)
    for a in ans:
        print(len(a), *a)
