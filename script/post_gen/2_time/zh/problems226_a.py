Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_query():
    N, Q = map(int, input().split())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    return N, Q, query

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

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 4

def main():
    n,q = map(int,input().split())
    trains = [0] * n
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            x,y = map(int,query[1:])
            if trains[x-1] == 0 and trains[y-1] == 0:
                trains[x-1] = y
                trains[y-1] = x
            elif trains[x-1] != 0 and trains[y-1] == 0:
                trains[y-1] = x
                trains[x-1] = trains[trains[x-1]-1]
            elif trains[x-1] == 0 and trains[y-1] != 0:
                trains[x-1] = y
                trains[y-1] = trains[trains[y-1]-1]
            elif trains[x-1] != 0 and trains[y-1] != 0:
                trains[x-1] = trains[trains[x-1]-1]
                trains[y-1] = trains[trains[y-1]-1]
        elif query[0] == '2':
            x,y = map(int,query[1:])
            if trains[x-1] == y:
                trains[x-1] = 0
                trains[y-1] = 0
            elif trains[x-1] != y:
                trains[x-1] = trains[trains[x-1]-1]
                trains[y-1] = trains[trains[y-1]-1]
        elif query[0] == '3':
            x = int(query[1])
            answer = []
            while trains[x-1] != 0:
                answer.append(str(x))
                x = trains[x-1]
            answer.append(str(x))
            print(len(answer),' '.join(answer))
main()

=======
Suggestion 5

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]
