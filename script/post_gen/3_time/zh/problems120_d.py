Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(N)
    print(M)
    print(A)
    print(B)
    return 0

=======
Suggestion 3

def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(a)
    print(b)
    print(m)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N)
    print(M)
    print(A)
    print(B)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    #print(AB)
    #print(N, M)
    #print(AB)
    ans = 0
    for i in range(M):
        a = AB[i][0]
        b = AB[i][1]
        if a > b:
            a, b = b, a
        if a == 1 and b == N:
            ans += 1
        elif a == 1 or b == N:
            ans += 2
        else:
            ans += 2
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print("N={}, M={}, A={}, B={}".format(N, M, A, B))
    return

=======
Suggestion 8

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 9

def find_root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]
