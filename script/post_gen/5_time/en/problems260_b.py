Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([i+1, A[i], B[i], A[i] + B[i]])
    C.sort(key=lambda x: x[3], reverse=True)
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    for i in range(X+Y+Z):
        print(C[i][0])

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = []
    for i in range(N):
        AB.append([i+1, A[i], B[i], A[i]+B[i]])
    AB.sort(key=lambda x: x[3], reverse=True)
    AB.sort(key=lambda x: x[2], reverse=True)
    AB.sort(key=lambda x: x[1], reverse=True)

    AB = AB[:X+Y+Z]

    AB.sort(key=lambda x: x[0])

    for i in range(len(AB)):
        print(AB[i][0])

=======
Suggestion 3

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = [(A[i], B[i], i+1) for i in range(N)]
    AB.sort(key = lambda x: x[2])
    AB.sort(key = lambda x: x[1], reverse=True)
    AB.sort(key = lambda x: x[0], reverse=True)
    for i in range(X):
        print(AB[i][2])
    for i in range(Y):
        print(AB[i+X][2])
    for i in range(Z):
        print(AB[i+X+Y][2])

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [i for i in range(1, N+1)]
    D = list(zip(C, A, B))
    D.sort(key=lambda x: x[2], reverse=True)
    D.sort(key=lambda x: x[1], reverse=True)
    D.sort(key=lambda x: x[1]+x[2], reverse=True)
    for i in range(X+Y+Z):
        print(D[i][0])

=======
Suggestion 5

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [i for i in range(1, n + 1)]
    d = list(zip(a, b, c))
    d.sort(key=lambda x: x[2], reverse=True)
    d.sort(key=lambda x: x[1], reverse=True)
    d.sort(key=lambda x: x[0], reverse=True)
    print(*[i[2] for i in d[:x]], sep="\n")

=======
Suggestion 6

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(zip(range(1, n+1), a, b))
    c = sorted(c, key=lambda x: -x[1])
    c = sorted(c[:x+y+z], key=lambda x: -x[2]-x[1])
    for i in range(x+y+z):
        print(c[i][0])

=======
Suggestion 7

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_B = []
    for i in range(N):
        A_B.append([A[i], B[i], i+1])
    A_B.sort(key=lambda x: x[2])
    A_B.sort(key=lambda x: x[1], reverse=True)
    A_B.sort(key=lambda x: x[0], reverse=True)
    for i in range(X):
        print(A_B[i][2])
    for i in range(Y):
        print(A_B[X+i][2])
    for i in range(Z):
        print(A_B[X+Y+i][2])

=======
Suggestion 8

def main():
    # Get input
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Solve
    c = []
    for i in range(n):
        c.append([i+1, a[i], b[i], a[i]+b[i]])

    c.sort(key=lambda x: x[3], reverse=True)
    c.sort(key=lambda x: x[2], reverse=True)
    c.sort(key=lambda x: x[1], reverse=True)

    output = []
    for i in range(x):
        output.append(c[i][0])

    for i in range(y):
        output.append(c[i+x][0])

    for i in range(z):
        output.append(c[i+x+y][0])

    output.sort()

    # Print result
    for i in range(len(output)):
        print(output[i])

=======
Suggestion 9

def main():
    # Get input
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Sort by score
    c = []
    for i in range(n):
        c.append([i + 1, a[i], b[i]])
    c.sort(key=lambda x: x[1] + x[2], reverse=True)

    # Admit
    d = []
    for i in range(x):
        d.append(c[i][0])
    for i in range(x, x + y):
        d.append(c[i][0])
    for i in range(x + y, x + y + z):
        d.append(c[i][0])
    d.sort()

    # Print output
    for i in range(len(d)):
        print(d[i])
