Synthesizing 10/10 solutions

=======
Suggestion 1

def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1
pascal_triangle(10)

=======
Suggestion 2

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

n = int(input())
triangle = pascal_triangle(n)
for row in triangle:
    for item in row:
        print(item, end=' ')
    print()

=======
Suggestion 3

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

=======
Suggestion 4

def main():
    n = int(input())
    a = [[1]]
    for i in range(1, n):
        a.append([1])
        for j in range(1, i):
            a[i].append(a[i-1][j-1] + a[i-1][j])
        a[i].append(1)
    for i in range(n):
        print(*a[i])

=======
Suggestion 5

def pascal_triangle(n):
    result = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)
    return result

n = int(input())
result = pascal_triangle(n)

for row in result:
    print(' '.join(map(str, row)))

=======
Suggestion 6

def print_pascal_triangle(n):
    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end = " ")
            C = int(C * (line - i) / i)
        print()

=======
Suggestion 7

def problem254_b():
    N = int(input())
    A = [[1 for j in range(i+1)] for i in range(N)]
    for i in range(2,N):
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(' '.join(map(str,A[i])))

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([0 for j in range(i+1)])
        for j in range(i+1):
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
        print(' '.join(map(str, A[i])))

=======
Suggestion 9

def pascal_triangle(n):
    a = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i+1):
            if (j == 0 or j == i):
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a

n = int(input())
a = pascal_triangle(n)
for i in range(n):
    for j in range(i+1):
        if j == i:
            print(a[i][j])
        else:
            print(a[i][j], end=" ")

=======
Suggestion 10

def f(n):
    if n == 0:
        return [1]
    else:
        a = f(n-1)
        return [1] + [a[i-1] + a[i] for i in range(1, n)] + [1]

n = int(input())
for i in range(n):
    print(*f(i))
