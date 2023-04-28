Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    #print(N, Q)
    #print(T)
    #print(A)
    #print(B)

    follow = [[0 for i in range(N)] for j in range(N)]

    for i in range(Q):
        if T[i] == 1:
            follow[A[i] - 1][B[i] - 1] = 1
        elif T[i] == 2:
            follow[A[i] - 1][B[i] - 1] = 0
        elif T[i] == 3:
            if follow[A[i] - 1][B[i] - 1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    follow = []
    for i in range(N):
        follow.append([])

    for i in range(Q):
        if T[i] == 1:
            follow[A[i]-1].append(B[i])
        elif T[i] == 2:
            if B[i] in follow[A[i]-1]:
                follow[A[i]-1].remove(B[i])
        elif T[i] == 3:
            if B[i] in follow[A[i]-1] and A[i] in follow[B[i]-1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            uf.union(a, b)
        elif t == 2:
            uf.unite(a, b)
        else:
            print('Yes' if uf.same(a, b) else 'No')

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    follow = [set() for _ in range(n)]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[a-1].discard(b-1)
        else:
            if a-1 in follow[b-1] and b-1 in follow[a-1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = [0] * N
    for _ in range(Q):
        T, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if T == 1:
            A[a] |= 1 << b
        elif T == 2:
            A[a] &= ~(1 << b)
        else:
            if A[a] & (1 << b):
                print("Yes")
            else:
                print("No")

=======
Suggestion 6

def main():
    # Get input here
    N, Q = map(int, input().strip().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().strip().split())
        T.append(t)
        A.append(a)
        B.append(b)
    # Solve problems
    # Initialize
    # Set
    # Print answer
    return

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    follow = [False] * N
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a - 1] = True
        elif t == 2:
            follow[a - 1] = False
        else:
            print('Yes' if follow[a - 1] and follow[b - 1] else 'No')

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    f = [ set() for _ in range(n) ]
    for _ in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            f[a-1].add(b-1)
        elif t == 2:
            f[a-1].discard(b-1)
        else:
            print("Yes" if b-1 in f[a-1] else "No")

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    user_list = []
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            if (a,b) not in user_list:
                user_list.append((a,b))
        elif t == 2:
            if (a,b) in user_list:
                user_list.remove((a,b))
        elif t == 3:
            if (a,b) in user_list and (b,a) in user_list:
                print("Yes")
            else:
                print("No")

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    #print(type(N))
    #print(type(Q))
    #print(type(input().split()))
    #print(type(map(int, input().split())))
    #print(type(list(map(int, input().split()))))
    #print(type(list(map(int, input().split()))[0]))
    #print(type(list(map(int, input().split()))[1]))
    #print(type(list(map(int, input().split()))[2]))
    #print(type(list(map(int, input().split()))[3]))
    #print(type(list(map(int, input().split()))[4]))
    #print(type(list(map(int, input().split()))[5]))
    #print(type(list(map(int, input().split()))[6]))
    #print(type(list(map(int, input().split()))[7]))
    #print(type(list(map(int, input().split()))[8]))
    #print(type(list(map(int, input().split()))[9]))
    #print(type(list(map(int, input().split()))[10]))
    #print(type(list(map(int, input().split()))[11]))
    #print(type(list(map(int, input().split()))[12]))
    #print(type(list(map(int, input().split()))[13]))
    #print(type(list(map(int, input().split()))[14]))
    #print(type(list(map(int, input().split()))[15]))
    #print(type(list(map(int, input().split()))[16]))
    #print(type(list(map(int, input().split()))[17]))
    #print(type(list(map(int, input().split()))[18]))
    #print(type(list(map(int, input().split()))[19]))
    #print(type(list(map(int, input().split()))[20]))
    #print(type(list(map(int, input().split()))[21]))
    #print(type(list(map(int, input().split()))[22]))
    #print(type(list(map(int, input().split()))[23]))
    #print(type(list(map(int, input().split()))[24]))
    #print(type(list(map(int, input().split()))[25]))
    #print(type(list(map(int, input().split()))[26]))
    #print(type(list(map(int, input().split()))[27]))
    #print(type(list(map(int, input().split()))[28]))
