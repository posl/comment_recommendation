Synthesizing 10/10 solutions

=======
Suggestion 1

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
        print(*a[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = [[1 for j in range(i+1)] for i in range(n)]
    for i in range(2,n):
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        print(' '.join(map(str,a[i])))

=======
Suggestion 3

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    a[0][0] = 1
    for i in range(1, n):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            if j == i:
                print(a[i][j])
            else:
                print(a[i][j], end=" ")

=======
Suggestion 4

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    a[0][0] = 1
    for i in range(1, n):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        print(" ".join([str(a[i][j]) for j in range(i+1)]))

=======
Suggestion 5

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(n):
        for j in range(i + 1):
            print(a[i][j], end=' ')
        print()

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([1]*(i+1))
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(*A[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = [[0 for i in range(n+1)] for j in range(n+1)]
    a[0][0] = 1
    for i in range(1,n+1):
        a[i][0] = 1
        for j in range(1,i+1):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j],end=" ")
        print()

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([1] * (i + 1))
    for i in range(2, N):
        for j in range(1, i):
            A[i][j] = A[i - 1][j - 1] + A[i - 1][j]
    for i in range(N):
        print(' '.join(map(str, A[i])))

=======
Suggestion 9

def main():
    n = int(input())
    a = [[1] for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        a[i].append(1)
    for i in range(n):
        print(*a[i])
main()

=======
Suggestion 10

def pascal_triangle(n):
    pascal = [[1]]
    for i in range(n-1):
        new_list = [1]
        for j in range(i):
            new_list.append(pascal[-1][j] + pascal[-1][j+1])
        new_list.append(1)
        pascal.append(new_list)
    return pascal

n = int(input())
pascal = pascal_triangle(n)

for i in range(n):
    print(*pascal[i])
