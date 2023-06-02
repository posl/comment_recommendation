Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

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
    N, Q = map(int, input().split())
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i] = i - 1
        B[i] = i + 1
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[B[query[1]]] = A[query[1]]
            B[A[query[1]]] = B[query[1]]
            B[query[1]] = B[query[2]]
            A[B[query[2]]] = query[1]
            A[query[1]] = query[2]
            B[query[2]] = query[1]
        elif query[0] == 2:
            A[B[query[1]]] = A[query[1]]
            B[A[query[1]]] = B[query[1]]
            B[query[1]] = A[query[2]]
            A[B[query[2]]] = query[1]
            A[query[1]] = query[2]
            B[query[2]] = query[1]
        else:
            ans = []
            x = B[0]
            while x <= N:
                ans.append(x)
                x = B[x]
            print(' '.join(map(str, ans)))

=======
Suggestion 4

def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

=======
Suggestion 5

def query1(l, x, y):
    if l[x-1][0] == 0 and l[y-1][1] == 0:
        l[x-1][0], l[y-1][1] = y, x
    elif l[x-1][0] == 0 and l[y-1][1] != 0:
        l[x-1][0], l[y-1][1] = l[y-1][1], x
    elif l[x-1][0] != 0 and l[y-1][1] == 0:
        l[x-1][0], l[y-1][1] = y, l[x-1][0]
    elif l[x-1][0] != 0 and l[y-1][1] != 0:
        l[x-1][0], l[y-1][1] = l[y-1][1], l[x-1][0]
    return l

=======
Suggestion 6

def find_root(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find_root(parent[x])
        return parent[x]
