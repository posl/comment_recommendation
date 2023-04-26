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

def main():
    N, Q = map(int, input().split())
    trains = [[] for _ in range(N)]
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1]) - 1
            y = int(query[2]) - 1
            trains[x].append(y)
            trains[y].append(x)
        elif query[0] == "2":
            x = int(query[1]) - 1
            y = int(query[2]) - 1
            trains[x].remove(y)
            trains[y].remove(x)
        else:
            x = int(query[1]) - 1
            print(*[a + 1 for a in trains[x]])

=======
Suggestion 3

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x]) 
        return parent[x]

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    train = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        train[i][0] = i - 1
        train[i][1] = i + 1
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[train[query[1]][0]][1] = train[query[1]][1]
            train[train[query[1]][1]][0] = train[query[1]][0]
            train[query[1]][0] = train[query[2]][0]
            train[query[1]][1] = query[2]
            train[train[query[2]][0]][1] = query[1]
            train[query[2]][0] = query[1]
        elif query[0] == 2:
            train[train[query[1]][0]][1] = train[query[2]][0]
            train[train[query[2]][0]][0] = train[query[1]][0]
            train[train[query[2]][1]][0] = query[1]
            train[query[2]][0] = query[1]
            train[query[1]][0] = train[query[2]][1]
            train[query[1]][1] = query[2]
        else:
            ans = []
            now = query[1]
            while now != 0:
                ans.append(now)
                now = train[now][1]
            print(' '.join(map(str, ans)))

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    #print(query)
    train = [i for i in range(n+1)]
    #print(train)
    for i in range(q):
        if query[i][0] == 1:
            train[query[i][1]] = query[i][2]
        elif query[i][0] == 2:
            train[query[i][1]] = query[i][1]
        else:
            print(train[query[i][1]])
