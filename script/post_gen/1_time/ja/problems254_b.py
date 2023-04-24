Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [[1] * (i+1) for i in range(N)]
    for i in range(N):
        for j in range(1, i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(*A[i])

=======
Suggestion 2

def main():
    N = int(input())
    a = [[1] * (i+1) for i in range(N)]
    for i in range(2, N):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(N):
        print(" ".join(map(str, a[i])))

=======
Suggestion 3

def main():
    N = int(input())
    A = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j==0 or j==i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        for j in range(i+1):
            print(A[i][j],end=" ")
        print()

=======
Suggestion 4

def main():
    n = int(input())
    a = [[1 for i in range(0, j + 1)] for j in range(0, n)]
    for i in range(1, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(0, n):
        for j in range(0, i + 1):
            print(a[i][j], end = ' ')
        print()

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                print(1,end=' ')
            else:
                print(A[i-1][j-1]+A[i-1][j],end=' ')
        print()
        A.append([1]*(i+1))

=======
Suggestion 6

def pascal_triangle(n):
    if n == 1:
        return [1]
    else:
        p = pascal_triangle(n-1)
        return [1] + [p[i]+p[i+1] for i in range(n-2)] + [1]

N = int(input())
for i in range(N):
    print(*pascal_triangle(i+1))

=======
Suggestion 7

def main():
    N = int(input())
    A = [1]
    for _ in range(N):
        print(*A)
        A = [1] + [A[i] + A[i+1] for i in range(len(A)-1)] + [1]

=======
Suggestion 8

def main():
    N = int(input())
    #N = 3
    #N = 10
    a = [[1] * i for i in range(1, N + 1)]
    for i in range(1, N):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(N):
        print(*a[i])

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(n):
        print(*pascal_triangle(i+1))

=======
Suggestion 10

def main():
    N = int(input())
    for i in range(N):
        #print(i)
        if i == 0:
            print(1)
        else:
            print(' '.join(map(str, a)))
        a = [1] * (i+1)
        for j in range(1, i):
            a[j] = a[j-1] + a[j]
main()
