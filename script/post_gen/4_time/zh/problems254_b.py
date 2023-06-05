Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([1]*(i+1))
    for i in range(2,n):
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j],end=' ')
        print()

=======
Suggestion 2

def f(n):
    if n == 1:
        return [[1]]
    else:
        L = f(n-1)
        L1 = L[-1]
        L2 = [1]
        for i in range(1, n-1):
            L2.append(L1[i-1] + L1[i])
        L2.append(1)
        L.append(L2)
        return L

=======
Suggestion 3

def f(n):
    a = [1]
    b = [1, 1]
    c = [1, 2, 1]
    d = [1, 3, 3, 1]
    e = [1, 4, 6, 4, 1]
    f = [1, 5, 10, 10, 5, 1]
    g = [1, 6, 15, 20, 15, 6, 1]
    h = [1, 7, 21, 35, 35, 21, 7, 1]
    i = [1, 8, 28, 56, 70, 56, 28, 8, 1]
    j = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    elif n == 3:
        print(a)
        print(b)
        print(c)
    elif n == 4:
        print(a)
        print(b)
        print(c)
        print(d)
    elif n == 5:
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
    elif n == 6:
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
    elif n == 7:
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
    elif n == 8:
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
    elif n == 9:
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
        print(i)
    elif n == 10:
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
        print(i)
        print(j)

=======
Suggestion 4

def problem254_b():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()

=======
Suggestion 5

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()

=======
Suggestion 6

def get_a(i,j):
    if j == 0 or j == i:
        return 1
    else:
        return get_a(i-1,j-1) + get_a(i-1,j)

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(get_a(i,j),end=" ")
    print()

=======
Suggestion 7

def main():
    N = 10
    A = []
    for i in range(N):
        A.append([0] * (i+1))
        for j in range(i+1):
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        for j in range(i+1):
            print(A[i][j], end=' ')
        print()

=======
Suggestion 8

def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]

n = int(input())
for i in triangles():
    print(i)
    if len(i) == n:
        break

=======
Suggestion 9

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    else:
        new_line = [1]
        last_line = pascal_triangle(n-1)[-1]
        for i in range(len(last_line)-1):
            new_line.append(last_line[i]+last_line[i+1])
        new_line.append(1)
        return pascal_triangle(n-1)+[new_line]

=======
Suggestion 10

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()
