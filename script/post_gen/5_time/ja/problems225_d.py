Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    train = [[] for _ in range(N)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1].append(query[2])
            train[query[2]-1].append(query[1])
        elif query[0] == 2:
            train[query[1]-1].remove(query[2])
            train[query[2]-1].remove(query[1])
        else:
            print(*train[query[1]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    trains = [[i, i] for i in range(N)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            if trains[query[1]-1][1] == trains[query[2]-1][0]:
                continue
            else:
                trains[trains[query[1]-1][1]-1][0] = trains[query[2]-1][0]
                trains[query[2]-1][0] = trains[query[1]-1][0]
                trains[query[1]-1][1] = trains[query[2]-1][1]
                trains[query[2]-1][1] = trains[trains[query[1]-1][1]-1][1]
        elif query[0] == 2:
            if trains[query[1]-1][1] == trains[query[2]-1][0]:
                trains[query[1]-1][1] = trains[query[2]-1][1]
                trains[trains[query[2]-1][1]-1][0] = trains[query[1]-1][1]
                trains[query[2]-1][1] = trains[query[1]-1][0]
                trains[trains[query[1]-1][0]-1][1] = trains[query[2]-1][1]
            else:
                continue
        elif query[0] == 3:
            output = []
            index = query[1]-1
            while True:
                output.append(index+1)
                if index == trains[index][1]-1:
                    break
                else:
                    index = trains[index][1]-1
            print(len(output), *output)
        else:
            continue

=======
Suggestion 4

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    train = [i for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            train[query[1]-1], train[query[2]-1] = train[query[2]-1], train[query[1]-1]
        elif query[0] == 2:
            for j in range(N):
                if train[j] == query[1]-1:
                    train[j] = query[2]-1
        else:
            ans = []
            for j in range(N):
                if train[j] == train[query[1]-1]:
                    ans.append(j+1)
            print(len(ans), *ans)

=======
Suggestion 6

def find(x):
  if par[x] < 0:
    return x
  else:
    par[x] = find(par[x])
    return par[x]
