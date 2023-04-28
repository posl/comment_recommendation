Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([i+1, A[i], B[i], A[i]+B[i]])
    C.sort(key=lambda x: x[3], reverse=True)
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[0])
    for i in range(X+Y+Z):
        print(C[i][0])

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append((i+1, A[i], B[i], A[i]+B[i]))
    C.sort(key=lambda x: x[3], reverse=True)
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    for i in range(X+Y+Z):
        print(C[i][0])

=======
Suggestion 3

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], i+1))
    c.sort(key=lambda x: x[2])
    c.sort(key=lambda x: x[1], reverse=True)
    c.sort(key=lambda x: x[0], reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x: x[2])
    for i in c:
        print(i[2])

=======
Suggestion 4

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i+1, a[i], b[i], a[i]+b[i]])
    c.sort(key=lambda x: x[3], reverse=True)
    c.sort(key=lambda x: x[2], reverse=True)
    c.sort(key=lambda x: x[1], reverse=True)
    for i in range(x+y+z):
        print(c[i][0])

=======
Suggestion 5

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = sorted(range(N), key=lambda k: C[k], reverse=True)
    E = sorted(D[:X])
    F = sorted(D[X:X+Y])
    G = sorted(D[X+Y:X+Y+Z])
    H = sorted(D[X+Y+Z:])
    print('\n'.join([str(i+1) for i in E+F+G]))

=======
Suggestion 6

def get_input():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, x, y, z, a, b

=======
Suggestion 7

def main():
    #N X Y Z
    #A_1 A_2 ... A_N
    #B_1 B_2 ... B_N
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append((A[i], B[i], i+1))
    C.sort(key=lambda x: -x[0])
    C = C[:X]
    C.sort(key=lambda x: -x[1])
    C = C[:X+Y]
    C.sort(key=lambda x: -(x[0]+x[1]))
    C = C[:X+Y+Z]
    C.sort(key=lambda x: x[2])
    for i in range(len(C)):
        print(C[i][2])

=======
Suggestion 8

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] + b[i] for i in range(n)]
    l = list(range(n))
    l.sort(key=lambda i: c[i], reverse=True)
    l = l[:x + y + z]
    l.sort()
    print(*[i + 1 for i in l], sep='\n')

=======
Suggestion 9

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [i for i in range(1, n+1)]
    d = list(zip(c, a, b))
    d.sort(key=lambda x: x[2], reverse=True)
    d.sort(key=lambda x: x[1], reverse=True)
    d.sort(key=lambda x: x[1]+x[2], reverse=True)

    for i in range(x+y+z):
        print(d[i][0])

=======
Suggestion 10

def problem260_b():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda x,y: x+y, A, B))
    D = list(zip(C, range(1,N+1)))
    D.sort(key=lambda x: x[1])
    D.sort(key=lambda x: x[0], reverse=True)
    for i in range(X):
        print(D[i][1])
    for i in range(X,X+Y):
        print(D[i][1])
    for i in range(X+Y,X+Y+Z):
        print(D[i][1])
